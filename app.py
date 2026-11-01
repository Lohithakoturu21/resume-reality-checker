import html
from typing import Dict, Set
import streamlit as st
from matcher import extract_text, find_skills, match, get_proven_skills
from suggestions import SUGGESTIONS


SAMPLE_JDS: Dict[str, str] = {
    "Custom (paste your own)": "",
    "Data Analyst Intern": (
        "Job Title: Data Analyst Intern\n"
        "Company: Analytics Insights Corp\n"
        "Location: Remote / Hybrid\n\n"
        "About the Role:\n"
        "We are looking for an ambitious Data Analyst Intern to join our business intelligence team. "
        "In this role, you will analyze large datasets, build interactive dashboards, and extract actionable business metrics.\n\n"
        "Key Responsibilities:\n"
        "- Extract, clean, and manipulate structured datasets using SQL and Python.\n"
        "- Perform exploratory data analysis using Pandas and NumPy to uncover operational trends.\n"
        "- Design, build, and maintain interactive business dashboards in Power BI and Tableau.\n"
        "- Utilize advanced Microsoft Excel (pivot tables, VLOOKUP) for quick data modeling and reporting.\n"
        "- Present data-driven insights to cross-functional teams with clear communication.\n\n"
        "Requirements & Qualifications:\n"
        "- Basic proficiency in Python for data analysis (experience with Pandas and NumPy).\n"
        "- Strong foundation in relational databases and querying using SQL (MySQL or PostgreSQL).\n"
        "- Hands-on familiarity with data visualization tools such as Power BI or Tableau.\n"
        "- Strong knowledge of Microsoft Excel for analytical modeling.\n"
        "- Solid problem solving skills, attention to detail, and effective teamwork."
    ),
    "Web Developer Intern": (
        "Job Title: Web Developer Intern\n"
        "Company: PixelCraft Digital Solutions\n"
        "Location: Remote / Hybrid\n\n"
        "About the Role:\n"
        "We are seeking an enthusiastic Web Developer Intern to assist our engineering teams in building responsive, "
        "user-friendly web applications. You will collaborate closely with senior developers and designers to implement clean user interfaces.\n\n"
        "Key Responsibilities:\n"
        "- Build responsive web pages using semantic HTML, modern CSS, and JavaScript.\n"
        "- Develop interactive web components and single-page applications utilizing React.\n"
        "- Integrate frontend interfaces with backend services via REST API endpoints.\n"
        "- Collaborate on codebase maintenance using Git and GitHub version control workflows.\n"
        "- Assist in testing, debugging, and optimizing web performance across different browsers.\n\n"
        "Requirements & Qualifications:\n"
        "- Good understanding of core web fundamentals: HTML, CSS, and modern JavaScript (ES6+).\n"
        "- Familiarity with TypeScript and component-based frontend libraries like React.\n"
        "- Basic understanding of backend technologies such as Node.js and Express.\n"
        "- Experience with version control tools: Git and GitHub.\n"
        "- Strong problem solving abilities, passion for clean UI design, and willingness to learn in an agile environment."
    ),
    "Python Developer Intern": (
        "Job Title: Python Developer Intern\n"
        "Company: CloudScale Technologies\n"
        "Location: Remote / Hybrid\n\n"
        "About the Role:\n"
        "CloudScale Technologies is looking for a motivated Python Developer Intern to join our backend software development team. "
        "You will contribute to writing clean backend code, designing scalable REST APIs, and automating deployment pipelines.\n\n"
        "Key Responsibilities:\n"
        "- Write robust, clean, and testable code in Python.\n"
        "- Develop and maintain scalable REST APIs using frameworks like FastAPI, Flask, or Django.\n"
        "- Design database schemas and write optimized queries for PostgreSQL and SQL databases.\n"
        "- Containerize application services using Docker and collaborate via Git and GitHub.\n"
        "- Support CI/CD integration and deployment to cloud infrastructure on Linux.\n\n"
        "Requirements & Qualifications:\n"
        "- Proficient understanding of Python syntax, data structures, and object-oriented programming.\n"
        "- Familiarity with web backend frameworks such as FastAPI, Flask, or Django.\n"
        "- Understanding of relational databases like SQL / PostgreSQL.\n"
        "- Basic knowledge of containerization with Docker and version control with Git.\n"
        "- Excellent problem solving mindset, effective communication, and eagerness to contribute to backend systems."
    ),
}


def generate_text_report(
    match_pct: float,
    verdict: str,
    advice: str,
    evidence_count_str: str,
    resume_skills: Set[str],
    matched_skills: Set[str],
    missing_skills: Set[str],
    proven_skills: Set[str],
    claimed_only: Set[str],
    suggestions: Dict[str, Dict[str, str]],
) -> str:
    """Generate a clean, structured plaintext report of the analysis."""
    lines = [
        "=" * 64,
        "             RESUME VS JOB REALITY CHECK REPORT             ",
        "=" * 64,
        "",
        "1. REALITY VERDICT & SCORE",
        "-" * 64,
        f"Skill Match Percentage : {match_pct:.1f}%",
        f"Reality Verdict        : {verdict}",
        f"Evidence Status        : {evidence_count_str}",
        f"Honest Advice          : {advice}",
        "",
        "2. MATCHED SKILLS",
        "-" * 64,
    ]

    if matched_skills:
        for s in sorted(matched_skills):
            lines.append(f"  [MATCH] {s}")
    else:
        lines.append("  (None)")

    lines.extend([
        "",
        "3. MISSING SKILLS",
        "-" * 64,
    ])
    if missing_skills:
        for s in sorted(missing_skills):
            lines.append(f"  [MISSING] {s}")
    else:
        lines.append("  (None - All required skills present!)")

    lines.extend([
        "",
        "4. CLAIMED VS PROVEN SKILLS",
        "-" * 64,
        "Recruiters trust skills that are backed by a project or experience.",
        "",
        f"Proven Skills ({len(proven_skills)}):",
    ])
    if proven_skills:
        for s in sorted(proven_skills):
            lines.append(f"  [PROVEN] {s}")
    else:
        lines.append("  (None)")

    lines.append(f"\nClaimed Only Skills ({len(claimed_only)}):")
    if claimed_only:
        for s in sorted(claimed_only):
            lines.append(f"  [CLAIMED ONLY] {s}")
    else:
        lines.append("  (None)")

    lines.extend([
        "",
        "5. LEARNING PLAN FOR MISSING SKILLS",
        "-" * 64,
    ])
    if missing_skills:
        for s in sorted(missing_skills):
            sug = suggestions.get(s.lower(), {})
            course = sug.get("course", "Recommended course")
            platform = sug.get("platform", "")
            project = sug.get("project") or sug.get("project_idea", "Beginner project idea")
            course_disp = f"{course} ({platform})" if platform and platform.lower() not in course.lower() else course

            lines.append(f"• Skill: {s.title()}")
            lines.append(f"  - Recommended Course : {course_disp}")
            lines.append(f"  - Beginner Project    : {project}")
            lines.append("")
    else:
        lines.append("  Great job! No upskilling needed for this position.")

    lines.extend([
        "=" * 64,
        "Generated by Resume vs Job Reality Checker",
        "=" * 64,
    ])
    return "\n".join(lines)


st.set_page_config(
    page_title="Resume vs Job Reality Checker",
    page_icon="📄",
    layout="wide",
)

# Custom styling for a polished theme across laptop screens
st.markdown(
    """
    <style>
    /* Centered Header & Tagline */
    h1 {
        text-align: center;
        margin-bottom: 0.2rem;
    }
    .tagline {
        text-align: center;
        font-size: 1.05rem;
        color: #475569;
        margin-top: -0.3rem;
        margin-bottom: 1.5rem;
    }
    /* Subtle metric text alignment */
    [data-testid="stMetricValue"] {
        font-size: 2.2rem;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📄 Resume vs Job Reality Checker")
st.markdown(
    '<p class="tagline">Bridge the gap between your resume and job requirements with instant matching, evidence checks & learning paths.</p>',
    unsafe_allow_html=True,
)

st.divider()

col_resume, col_jd = st.columns(2, gap="medium")

with col_resume:
    with st.container(border=True):
        st.subheader("1. Resume PDF")
        resume_file = st.file_uploader(
            "Upload Resume (PDF)",
            type=["pdf"],
            help="Upload your resume in PDF format",
        )

def on_sample_change():
    chosen = st.session_state.get("sample_choice")
    if chosen in SAMPLE_JDS:
        st.session_state["jd_text_area"] = SAMPLE_JDS[chosen]

if "jd_text_area" not in st.session_state:
    st.session_state["jd_text_area"] = ""

with col_jd:
    with st.container(border=True):
        st.subheader("2. Job Description")
        st.selectbox(
            "Sample Job Description",
            options=[
                "Custom (paste your own)",
                "Data Analyst Intern",
                "Web Developer Intern",
                "Python Developer Intern",
            ],
            key="sample_choice",
            on_change=on_sample_change,
            help="Select a sample job description to auto-fill or choose Custom to paste your own",
        )
        jd_text = st.text_area(
            "Job Description",
            key="jd_text_area",
            height=240,
            placeholder="Paste the job requirements or description here...",
        )

check_button = st.button("Check", type="primary", use_container_width=True)

if check_button:
    current_jd = st.session_state.get("jd_text_area", "")
    if not resume_file:
        st.error("Please upload a resume PDF file.")
    elif not current_jd.strip():
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
            jd_skills = find_skills(current_jd)
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

    # Match score and progress card
    with st.container(border=True):
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

    # Reality Verdict clear colored banner
    evidence_count_str = f"{len(proven_skills)} of {len(resume_skills)} skills are backed by projects."
    if match_pct >= 75:
        verdict_title = "Apply now"
        verdict_advice = "Your profile strongly aligns with the job requirements—tailor your resume highlights and submit your application with confidence!"
        st.success(
            f"**Reality Verdict: Apply now**\n\n"
            f"📌 **{evidence_count_str}**  \n\n"
            f"💡 *Honest Advice:* {verdict_advice}"
        )
    elif match_pct >= 40:
        verdict_title = "Upskill first, you are close"
        verdict_advice = "You have a solid foundation, but closing the gap on missing key skills will significantly improve your chances."
        st.warning(
            f"**Reality Verdict: Upskill first, you are close**\n\n"
            f"📌 **{evidence_count_str}**  \n\n"
            f"💡 *Honest Advice:* {verdict_advice}"
        )
    else:
        verdict_title = "Not ready yet"
        verdict_advice = "There is a substantial skill gap for this role; focus on foundational courses and practical beginner projects before applying."
        st.error(
            f"**Reality Verdict: Not ready yet**\n\n"
            f"📌 **{evidence_count_str}**  \n\n"
            f"💡 *Honest Advice:* {verdict_advice}"
        )

    # Display Extracted Resume Skills, Matched Skills, and Missing Skills in styled cards
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
        with st.container(border=True):
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
        with st.container(border=True):
            st.markdown(f"### ✅ Matched Skills ({len(matched_skills)})")
            render_badges(matched_skills, "green")

    with col3:
        with st.container(border=True):
            st.markdown(f"### ❌ Missing Skills ({len(missing_skills)})")
            render_badges(missing_skills, "red")

    # Learning Plan section
    st.divider()
    with st.container(border=True):
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

    # Download Report button
    report_text = generate_text_report(
        match_pct=match_pct,
        verdict=verdict_title,
        advice=verdict_advice,
        evidence_count_str=evidence_count_str,
        resume_skills=resume_skills,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        proven_skills=proven_skills,
        claimed_only=claimed_only,
        suggestions=SUGGESTIONS,
    )

    st.write("")
    st.download_button(
        label="📥 Download Reality Report",
        data=report_text,
        file_name="resume_reality_report.txt",
        mime="text/plain",
        use_container_width=True,
    )
