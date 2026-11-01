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


__all__ = ["SKILLS", "extract_text", "find_skills", "match"]
