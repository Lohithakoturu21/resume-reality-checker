"""Resume and Job Description Skill Matcher.

This module provides utilities to extract text from PDF resumes, extract recognized
skills using whole-word case-insensitive matching, and compute match analytics
between resume skills and job description skills.
"""

import io
import re
from typing import Any, Iterable, Set, Tuple
import pdfplumber

# Catalog of common technical and professional skills (~65 skills)
SKILLS = [
    # Programming Languages
    "python",
    "java",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "php",
    "ruby",
    "go",
    "rust",
    "kotlin",
    "swift",
    "scala",
    # Web & Frameworks
    "html",
    "css",
    "react",
    "angular",
    "vue",
    "node.js",
    "django",
    "flask",
    "fastapi",
    "spring boot",
    "express",
    "next.js",
    # Databases & Caching
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "redis",
    "oracle",
    # Cloud, DevOps & Infrastructure
    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "gcp",
    "linux",
    "terraform",
    "jenkins",
    "ci/cd",
    # Data Science, ML & AI
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "natural language processing",
    "computer vision",
    "data analysis",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    # Business Intelligence & Analytics
    "excel",
    "power bi",
    "tableau",
    # APIs & Architecture
    "rest api",
    "graphql",
    # Methodologies & Soft Skills
    "agile",
    "scrum",
    "communication",
    "problem solving",
    "leadership",
    "teamwork",
    "project management",
]


def _build_skill_pattern(skill: str) -> str:
    """Build a regex pattern to match a skill as a whole word case-insensitively."""
    # Special character edge-cases
    if skill == "c++":
        return r"(?<![A-Za-z0-9_])c\+\+(?![+\w])"
    if skill == "c#":
        return r"(?<![A-Za-z0-9_])c\#(?![#\w])"
    if skill == "node.js":
        return r"(?<![A-Za-z0-9_])node(?:\.js|js)(?![A-Za-z0-9_])"
    if skill == "next.js":
        return r"(?<![A-Za-z0-9_])next(?:\.js|js)(?![A-Za-z0-9_])"
    if skill == "ci/cd":
        return r"(?<![A-Za-z0-9_])ci\s*[/\\-]?\s*cd(?![A-Za-z0-9_])"

    # Multi-word skills: allow flexible whitespace between words
    parts = [re.escape(part) for part in skill.split()]
    skill_regex = r"\s+".join(parts)

    # Optional plural form if skill does not already end in 's' (e.g. 'rest api' matches 'rest apis')
    plural = r"s?" if not skill.endswith("s") else ""

    # Whole-word boundaries avoiding partial-word substring matches
    return rf"(?<![A-Za-z0-9_]){skill_regex}{plural}(?![A-Za-z0-9_])"


def extract_text(file: Any) -> str:
    """Extract and concatenate text from all pages of a PDF file using pdfplumber.

    Args:
        file: A file path string, Path object, or file-like object (e.g., Streamlit UploadedFile, BytesIO).

    Returns:
        Extracted text as a string.
    """
    if hasattr(file, "seek"):
        file.seek(0)

    if isinstance(file, bytes):
        file = io.BytesIO(file)

    text_pages = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_pages.append(page_text)

    return "\n".join(text_pages)


def find_skills(text: str) -> Set[str]:
    """Find recognized skills from SKILLS present in the provided text.

    Matches whole words case-insensitively and returns a set of matched skill names.

    Args:
        text: Input text string (from resume or job description).

    Returns:
        A set of skill names found in the text.
    """
    if not text or not isinstance(text, str):
        return set()

    found_skills: Set[str] = set()
    for skill in SKILLS:
        pattern = _build_skill_pattern(skill)
        if re.search(pattern, text, re.IGNORECASE):
            found_skills.add(skill)

    return found_skills


def match(resume_skills: Iterable[str], jd_skills: Iterable[str]) -> Tuple[float, Set[str], Set[str]]:
    """Compare skills extracted from a resume against skills required in a job description.

    Args:
        resume_skills: Iterable of skills found in the resume.
        jd_skills: Iterable of skills required by the job description.

    Returns:
        A tuple of:
            - match percentage: (matched / JD skills * 100), rounded to 2 decimal places.
            - matched skills: set of skills in both resume and JD.
            - missing skills: set of skills in JD that are missing from the resume.
    """
    resume_set: Set[str] = set(resume_skills) if resume_skills else set()
    jd_set: Set[str] = set(jd_skills) if jd_skills else set()

    matched = resume_set & jd_set
    missing = jd_set - resume_set

    if not jd_set:
        match_percentage = 0.0
    else:
        match_percentage = round((len(matched) / len(jd_set)) * 100.0, 2)

    return match_percentage, matched, missing


_SKILLS_HEADING_PATTERN = re.compile(
    r"^(?:"
    r"skills?|"
    r"technical\s+skills?|"
    r"key\s+skills?|"
    r"core\s+skills?|"
    r"professional\s+skills?|"
    r"computer\s+skills?|"
    r"it\s+skills?|"
    r"programming\s+skills?|"
    r"hard\s+skills?|"
    r"soft\s+skills?|"
    r"tech\s*stack|"
    r"technologies|"
    r"tools\s+(?:and|&)\s+technologies|"
    r"technologies\s+(?:and|&)\s+tools|"
    r"skills?\s+(?:and|&)\s+(?:tools|abilities|competencies|technologies|proficiencies|expertise)|"
    r"technical\s+proficiencies|"
    r"core\s+competencies|"
    r"areas\s+of\s+expertise|"
    r"competencies"
    r")$",
    re.IGNORECASE,
)

_NON_SKILLS_HEADING_PATTERN = re.compile(
    r"^(?:"
    r"(?:work\s+|professional\s+|relevant\s+|career\s+|employment\s+)?experience|"
    r"employment(?:\s+history)?|"
    r"work\s+history|"
    r"(?:academic\s+|personal\s+|key\s+|selected\s+|technical\s+|notable\s+)?projects?|"
    r"internships?(?:\s+experience)?|"
    r"education(?:\s+background|\s+history|\s+qualifications)?|"
    r"academic(?:\s+background|\s+qualifications|\s+history)?|"
    r"academics|"
    r"certifications?|"
    r"certificates?|"
    r"licenses?(?:\s+(?:and|&)\s+certifications?)?|"
    r"(?:professional\s+|executive\s+|career\s+)?summary|"
    r"profile|"
    r"personal\s+profile|"
    r"about(?:\s+me)?|"
    r"(?:career\s+)?objective|"
    r"awards?(?:\s+(?:and|&)\s+honors?)?|"
    r"honors?(?:\s+(?:and|&)\s+awards?)?|"
    r"achievements?|"
    r"accomplishments?|"
    r"publications?|"
    r"research(?:\s+experience)?|"
    r"volunteer(?:\s+experience|\s+work)?|"
    r"volunteering|"
    r"extracurricular(?:\s+activities)?|"
    r"activities|"
    r"leadership(?:\s+experience)?|"
    r"affiliations?|"
    r"memberships?|"
    r"interests?|"
    r"hobbies|"
    r"references?"
    r")$",
    re.IGNORECASE,
)


def _clean_line_for_heading(line: str) -> str:
    """Normalize line text by stripping markdown symbols, bullets, and punctuation."""
    cleaned = line.strip()
    cleaned = re.sub(r"^[\s#*\-–—•|>]+", "", cleaned)
    cleaned = re.sub(r"[\s*:\-–—|#]+$", "", cleaned)
    return cleaned.strip()


def _is_skills_heading(line: str) -> bool:
    """Check if a line represents a Skills section heading."""
    cleaned = _clean_line_for_heading(line)
    if not cleaned or len(cleaned.split()) > 5 or len(cleaned) > 40:
        return False
    if cleaned.endswith((".", ",", ";")):
        return False
    if _SKILLS_HEADING_PATTERN.match(cleaned):
        return True
    lower = cleaned.lower()
    if re.search(r"\b(skills?|tech\s*stack|technologies)\b", lower):
        if not re.search(r"\b(experience|projects?|work|internships?|education|summary|awards?)\b", lower):
            return True
    return False


def _is_non_skills_heading(line: str) -> bool:
    """Check if a line represents a non-skills section heading (e.g. Experience, Projects)."""
    cleaned = _clean_line_for_heading(line)
    if not cleaned or len(cleaned.split()) > 5 or len(cleaned) > 40:
        return False
    if cleaned.endswith((".", ",", ";")):
        return False
    if _NON_SKILLS_HEADING_PATTERN.match(cleaned):
        return True
    lower = cleaned.lower()
    if re.search(r"\b(experience|projects?|internships?|education|certif|training|courses?|summary|profile|awards?|publications?)\b", lower):
        return True
    if cleaned.isupper() and len(cleaned.split()) <= 4 and len(cleaned) <= 30:
        return True
    return False


def split_resume_sections(resume_text: str) -> Tuple[str, str]:
    """Split resume text into a skills section and an evidence section.

    Skills section: text under headings like Skills, Technical Skills.
    Evidence section: everything else (Projects, Experience, Internships, etc.).

    Args:
        resume_text: Raw text string of the resume.

    Returns:
        A tuple of (skills_section_text, evidence_section_text).
    """
    if not resume_text or not isinstance(resume_text, str):
        return "", ""

    skills_lines = []
    evidence_lines = []
    in_skills_section = False

    for line in resume_text.splitlines():
        trimmed = line.strip()
        if not trimmed:
            continue

        # Handle inline headings like "Technical Skills: Python, Java, Docker"
        inline_skills_match = re.match(
            r"^(technical\s+skills?|key\s+skills?|core\s+skills?|skills?|tech\s*stack|technologies)\s*:\s*(.+)$",
            trimmed,
            re.IGNORECASE,
        )
        if inline_skills_match:
            in_skills_section = True
            content_after = inline_skills_match.group(2).strip()
            if content_after:
                skills_lines.append(content_after)
            continue

        inline_evidence_match = re.match(
            r"^((?:work\s+|professional\s+)?experience|projects?|internships?|education)\s*:\s*(.+)$",
            trimmed,
            re.IGNORECASE,
        )
        if inline_evidence_match:
            in_skills_section = False
            evidence_lines.append(line)
            continue

        if _is_skills_heading(trimmed):
            in_skills_section = True
            continue
        elif in_skills_section and _is_non_skills_heading(trimmed):
            in_skills_section = False
            evidence_lines.append(line)
        elif in_skills_section:
            skills_lines.append(line)
        else:
            evidence_lines.append(line)

    return "\n".join(skills_lines), "\n".join(evidence_lines)


def get_proven_skills(resume_text: str) -> Tuple[Set[str], Set[str]]:
    """Determine proven skills vs claimed-only skills in a resume.

    Splits resume text into a skills section and an evidence section (such as
    Projects, Experience, Internships), returning:
    - proven: skills found in the evidence section.
    - claimed_only: skills found only in the skills section.

    Args:
        resume_text: Raw text of the resume.

    Returns:
        A tuple of (proven, claimed_only) sets.
    """
    if not resume_text or not isinstance(resume_text, str):
        return set(), set()

    skills_text, evidence_text = split_resume_sections(resume_text)
    proven = find_skills(evidence_text)
    skills_section_skills = find_skills(skills_text)
    claimed_only = skills_section_skills - proven

    return proven, claimed_only


__all__ = ["SKILLS", "extract_text", "find_skills", "match", "split_resume_sections", "get_proven_skills"]

