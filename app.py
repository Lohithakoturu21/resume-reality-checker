import html
import streamlit as st
from matcher import extract_text, find_skills, match, get_proven_skills
from suggestions import SUGGESTIONS



st.set_page_config(
    page_title="Resume vs Job Reality Checker",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume vs Job Reality Checker")
st.markdown(
    "Upload your resume PDF and paste a job description to instantly see your skill match score, "
    "matching skills, and missing skills."
)

st.divider()

col_resume, col_jd = st.columns(2, gap="large")

with col_resume:
    st.subheader("1. Resume PDF")
    resume_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"],
        help="Upload your resume in PDF format"
    )

with col_jd:
    st.subheader("2. Job Description")
    jd_text = st.text_area(
        "Job Description",
        height=240,
        placeholder="Paste the job requirements or description here..."
    )

check_button = st.button("Check", type="primary", use_container_width=True)

if check_button:
    if not resume_file:
        st.error("Please upload a resume PDF file.")
    elif not jd_text.strip():
        st.error("Please enter or paste a job description.")
    else:
        with st.spinner("Extracting text and analyzing skills..."):
            try:
                resume_text = extract_text(resume_file)
            except Exception as e:
                st.error(f"Failed to read PDF file: {e}")
                resume_text = ""

        if not resume_text.strip():
            st.warning(
                "Could not extract any readable text from the uploaded PDF. "
                "Please verify that the PDF contains selectable text (not scanned images)."
            )
        else:
            resume_skills = find_skills(resume_text)
            jd_skills = find_skills(jd_text)
            match_pct, matched_skills, missing_skills = match(resume_skills, jd_skills)
            proven_skills, claimed_only = get_proven_skills(resume_text)

            st.session_state["results"] = {
                "match_pct": match_pct,
                "resume_skills": resume_skills,
                "jd_skills": jd_skills,
                "matched_skills": matched_skills,
                "missing_skills": missing_skills,
                "proven_skills": proven_skills,
                "claimed_only": claimed_only,
                "resume_text": resume_text,
            }

if "results" in st.session_state:
    res = st.session_state["results"]
    match_pct = res["match_pct"]
    resume_skills = res["resume_skills"]
    jd_skills = res["jd_skills"]
    matched_skills = res["matched_skills"]
    missing_skills = res["missing_skills"]
    proven_skills = res.get("proven_skills")
    claimed_only = res.get("claimed_only")
    if proven_skills is None or claimed_only is None:
        if "resume_text" in res:
            proven_skills, claimed_only = get_proven_skills(res["resume_text"])
        else:
            proven_skills = set()
            claimed_only = set(resume_skills)

    st.divider()
    st.subheader("📊 Match Results")

    # Match percentage with progress bar
    col_score, col_details = st.columns([1, 2], gap="medium")

    with col_score:
        st.metric(label="Skill Match Percentage", value=f"{match_pct:.1f}%")

    with col_details:
        progress_val = min(max(float(match_pct) / 100.0, 0.0), 1.0)
        st.write(f"Matched **{len(matched_skills)}** of **{len(jd_skills)}** skills identified in the Job Description.")
        st.progress(progress_val)

    if not jd_skills:
        st.info(
            "ℹ️ No catalog skills were detected in the Job Description text. "
            "Ensure the JD mentions common technical or professional skills."
        )

    st.write("")

    # Reality Verdict box above the skill lists based on match percentage
    evidence_count_str = f"{len(proven_skills)} of {len(resume_skills)} skills are backed by projects."
    if match_pct >= 75:
        st.success(
            f"**Reality Verdict: Apply now**\n\n"
            f"{evidence_count_str} "
            f"Your profile strongly aligns with the job requirements—tailor your resume highlights and submit your application with confidence!"
        )
    elif match_pct >= 40:
        st.warning(
            f"**Reality Verdict: Upskill first, you are close**\n\n"
            f"{evidence_count_str} "
            f"You have a solid foundation, but closing the gap on missing key skills will significantly improve your chances."
        )
    else:
        st.error(
            f"**Reality Verdict: Not ready yet**\n\n"
            f"{evidence_count_str} "
            f"There is a substantial skill gap for this role; focus on foundational courses and practical beginner projects before applying."
        )

    # Display Extracted Resume Skills, Matched Skills, and Missing Skills
    col1, col2, col3 = st.columns(3, gap="medium")

    def render_badges(skills, badge_type):
        if not skills:
            st.markdown("*None*")
            return
        colors = {
            "blue": {"bg": "#e0f2fe", "text": "#0369a1", "border": "#7dd3fc"},
            "green": {"bg": "#dcfce7", "text": "#15803d", "border": "#86efac"},
            "red": {"bg": "#fee2e2", "text": "#b91c1c", "border": "#fca5a5"},
            "yellow": {"bg": "#fef9c3", "text": "#854d0e", "border": "#fde047"},
        }
        theme = colors.get(badge_type, colors["blue"])
        badges = " ".join([
            f'<span style="display:inline-block; margin:3px 4px; padding:4px 10px; border-radius:12px; '
            f'font-size:13px; font-weight:600; background-color:{theme["bg"]}; color:{theme["text"]}; '
            f'border:1px solid {theme["border"]};">{html.escape(s)}</span>'
            for s in sorted(skills)
        ])
        st.markdown(badges, unsafe_allow_html=True)

    with col1:
        st.markdown(f"### 📄 Extracted Resume Skills ({len(resume_skills)})")
        render_badges(resume_skills, "blue")

        st.write("")
        st.markdown("#### Claimed vs Proven")
        st.markdown("Recruiters trust skills that are backed by a project or experience.")
        st.markdown(f"**Proven Skills ({len(proven_skills)}):**")
        render_badges(proven_skills, "green")
        st.markdown(f"**Claimed Only ({len(claimed_only)}):**")
        render_badges(claimed_only, "yellow")

    with col2:
        st.markdown(f"### ✅ Matched Skills ({len(matched_skills)})")
        render_badges(matched_skills, "green")

    with col3:
        st.markdown(f"### ❌ Missing Skills ({len(missing_skills)})")
        render_badges(missing_skills, "red")

    # Learning Plan section
    st.divider()
    st.subheader("Learning Plan")
    if missing_skills:
        for skill in sorted(missing_skills):
            suggestion = SUGGESTIONS.get(skill.lower(), {})
            course = suggestion.get("course", "Recommended course")
            platform = suggestion.get("platform", "")
            project = suggestion.get("project") or suggestion.get("project_idea", "Beginner project idea")

            if platform and platform.lower() not in course.lower():
                course_display = f"{course} ({platform})"
            else:
                course_display = course

            with st.expander(skill.title()):
                st.markdown(f"**Course:** {course_display}")
                st.markdown(f"**Project Idea:** {project}")
    else:
        st.success("🎉 No missing skills detected! You meet all the catalog skill requirements for this position.")

