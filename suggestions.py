"""Learning Suggestions and Project Ideas for Skills Catalog.

Provides recommended free courses (with platforms like Coursera, freeCodeCamp,
YouTube, NPTEL) and beginner project ideas for every skill in the SKILLS catalog.
"""

from typing import Any, Dict

SKILL_SUGGESTIONS: Dict[str, Dict[str, str]] = {
    # Programming Languages
    "python": {
        "course": "Programming for Everybody (Getting Started with Python)",
        "platform": "Coursera",
        "project": "Build a command-line expense tracker that records daily spending and exports summary reports to a CSV file.",
        "project_idea": "Build a command-line expense tracker that records daily spending and exports summary reports to a CSV file.",
    },
    "java": {
        "course": "Java Programming for Beginners",
        "platform": "freeCodeCamp",
        "project": "Create a console-based bank account management system supporting deposits, withdrawals, and balance inquiries.",
        "project_idea": "Create a console-based bank account management system supporting deposits, withdrawals, and balance inquiries.",
    },
    "c++": {
        "course": "C++ Tutorial for Beginners",
        "platform": "freeCodeCamp",
        "project": "Develop a text-based inventory management system using object-oriented principles and file I/O.",
        "project_idea": "Develop a text-based inventory management system using object-oriented principles and file I/O.",
    },
    "c#": {
        "course": "C# Tutorial for Beginners",
        "platform": "freeCodeCamp",
        "project": "Build a desktop to-do list manager with task prioritization and local file persistence using .NET.",
        "project_idea": "Build a desktop to-do list manager with task prioritization and local file persistence using .NET.",
    },
    "javascript": {
        "course": "JavaScript Algorithms and Data Structures",
        "platform": "freeCodeCamp",
        "project": "Create an interactive quiz application with a dynamic timer, score tracking, and local storage persistence.",
        "project_idea": "Create an interactive quiz application with a dynamic timer, score tracking, and local storage persistence.",
    },
    "typescript": {
        "course": "TypeScript Course for Beginners",
        "platform": "freeCodeCamp",
        "project": "Build a type-safe shopping cart with item quantity adjustments and discount code validation.",
        "project_idea": "Build a type-safe shopping cart with item quantity adjustments and discount code validation.",
    },
    "php": {
        "course": "PHP for Beginners",
        "platform": "freeCodeCamp",
        "project": "Develop a simple blog CMS where users can create, edit, delete, and view posts stored in a MySQL database.",
        "project_idea": "Develop a simple blog CMS where users can create, edit, delete, and view posts stored in a MySQL database.",
    },
    "ruby": {
        "course": "Ruby Programming Course",
        "platform": "freeCodeCamp",
        "project": "Build a terminal-based flashcard quiz tool that tracks correct answers and spaced repetition stats.",
        "project_idea": "Build a terminal-based flashcard quiz tool that tracks correct answers and spaced repetition stats.",
    },
    "go": {
        "course": "Go Programming by Example",
        "platform": "freeCodeCamp",
        "project": "Create a concurrent URL status checker that pings multiple websites simultaneously and logs response times.",
        "project_idea": "Create a concurrent URL status checker that pings multiple websites simultaneously and logs response times.",
    },
    "rust": {
        "course": "Rust Programming Course for Beginners",
        "platform": "freeCodeCamp",
        "project": "Build a command-line grep tool that searches for string patterns within text files.",
        "project_idea": "Build a command-line grep tool that searches for string patterns within text files.",
    },
    "kotlin": {
        "course": "Kotlin Course for Beginners",
        "platform": "freeCodeCamp",
        "project": "Develop an Android simple note-taking app with SQLite/Room database storage.",
        "project_idea": "Develop an Android simple note-taking app with SQLite/Room database storage.",
    },
    "swift": {
        "course": "Swift Programming Tutorial",
        "platform": "freeCodeCamp",
        "project": "Create a simple iOS tip calculator app with custom bill splitting and percentage selection.",
        "project_idea": "Create a simple iOS tip calculator app with custom bill splitting and percentage selection.",
    },
    "scala": {
        "course": "Functional Programming Principles in Scala",
        "platform": "Coursera",
        "project": "Write a functional log file analyzer that filters and computes statistics on server access logs.",
        "project_idea": "Write a functional log file analyzer that filters and computes statistics on server access logs.",
    },

    # Web & Frameworks
    "html": {
        "course": "Responsive Web Design Certification",
        "platform": "freeCodeCamp",
        "project": "Build a semantic personal portfolio page highlighting your bio, projects, and contact links.",
        "project_idea": "Build a semantic personal portfolio page highlighting your bio, projects, and contact links.",
    },
    "css": {
        "course": "CSS Full Course for Beginners",
        "platform": "freeCodeCamp",
        "project": "Design a responsive product landing page with CSS Flexbox, Grid, and smooth hover animations.",
        "project_idea": "Design a responsive product landing page with CSS Flexbox, Grid, and smooth hover animations.",
    },
    "react": {
        "course": "React for Beginners",
        "platform": "freeCodeCamp",
        "project": "Create a task tracking Kanban board with drag-and-drop tasks, categories, and state management.",
        "project_idea": "Create a task tracking Kanban board with drag-and-drop tasks, categories, and state management.",
    },
    "angular": {
        "course": "Angular Full Course",
        "platform": "freeCodeCamp",
        "project": "Build a weather forecast dashboard that fetches and displays live data from a public weather API.",
        "project_idea": "Build a weather forecast dashboard that fetches and displays live data from a public weather API.",
    },
    "vue": {
        "course": "Vue.js 3 Fundamentals",
        "platform": "freeCodeCamp",
        "project": "Build a personal recipe book application with search, ingredient filters, and reactive forms.",
        "project_idea": "Build a personal recipe book application with search, ingredient filters, and reactive forms.",
    },
    "node.js": {
        "course": "Node.js and Express.js Full Course",
        "platform": "freeCodeCamp",
        "project": "Build a backend CRUD REST API for a book collection with JSON file persistence.",
        "project_idea": "Build a backend CRUD REST API for a book collection with JSON file persistence.",
    },
    "django": {
        "course": "Django for Everybody Specialization",
        "platform": "Coursera",
        "project": "Create a multi-user polling and voting web application with an admin dashboard and authentication.",
        "project_idea": "Create a multi-user polling and voting web application with an admin dashboard and authentication.",
    },
    "flask": {
        "course": "Python Flask for Beginners",
        "platform": "freeCodeCamp",
        "project": "Build a URL shortener service that maps custom short codes to URLs using SQLite.",
        "project_idea": "Build a URL shortener service that maps custom short codes to URLs using SQLite.",
    },
    "fastapi": {
        "course": "FastAPI Course for Beginners",
        "platform": "freeCodeCamp",
        "project": "Create an asynchronous student management API with Swagger docs and Pydantic data validation.",
        "project_idea": "Create an asynchronous student management API with Swagger docs and Pydantic data validation.",
    },
    "spring boot": {
        "course": "Spring Boot Tutorial for Beginners",
        "platform": "freeCodeCamp",
        "project": "Develop an employee directory REST service with H2 in-memory database and CRUD endpoints.",
        "project_idea": "Develop an employee directory REST service with H2 in-memory database and CRUD endpoints.",
    },
    "express": {
        "course": "Node.js & Express - Full Tutorial",
        "platform": "freeCodeCamp",
        "project": "Build a user authentication API with JWT tokens, password hashing, and protected routes.",
        "project_idea": "Build a user authentication API with JWT tokens, password hashing, and protected routes.",
    },
    "next.js": {
        "course": "Next.js Full Course",
        "platform": "freeCodeCamp",
        "project": "Build a static developer portfolio and blog using Next.js App Router and Markdown (MDX) rendering.",
        "project_idea": "Build a static developer portfolio and blog using Next.js App Router and Markdown (MDX) rendering.",
    },

    # Databases & Caching
    "sql": {
        "course": "Intro to SQL: Querying and Managing Data",
        "platform": "Khan Academy",
        "project": "Design an e-commerce database schema and write analytical queries for sales, top customers, and stock.",
        "project_idea": "Design an e-commerce database schema and write analytical queries for sales, top customers, and stock.",
    },
    "mysql": {
        "course": "MySQL Database - Full Course",
        "platform": "freeCodeCamp",
        "project": "Create a relational database for a library system with tables for books, members, and loans.",
        "project_idea": "Create a relational database for a library system with tables for books, members, and loans.",
    },
    "postgresql": {
        "course": "PostgreSQL Tutorial for Beginners",
        "platform": "freeCodeCamp",
        "project": "Build a geospatial store locator querying nearest locations using Postgres and SQL joins.",
        "project_idea": "Build a geospatial store locator querying nearest locations using Postgres and SQL joins.",
    },
    "mongodb": {
        "course": "MongoDB Complete Tutorial",
        "platform": "freeCodeCamp",
        "project": "Build a product catalog database with nested category attributes and aggregation queries.",
        "project_idea": "Build a product catalog database with nested category attributes and aggregation queries.",
    },
    "redis": {
        "course": "Redis Crash Course",
        "platform": "freeCodeCamp",
        "project": "Implement a Redis-backed rate limiter and caching layer for an API endpoint.",
        "project_idea": "Implement a Redis-backed rate limiter and caching layer for an API endpoint.",
    },
    "oracle": {
        "course": "Database Management System",
        "platform": "NPTEL",
        "project": "Write PL/SQL stored procedures and triggers to automate order status updates in an inventory database.",
        "project_idea": "Write PL/SQL stored procedures and triggers to automate order status updates in an inventory database.",
    },

    # Cloud, DevOps & Infrastructure
    "git": {
        "course": "Git and GitHub for Beginners",
        "platform": "freeCodeCamp",
        "project": "Initialize a repository, practice branching, resolving merge conflicts, and tagging release versions.",
        "project_idea": "Initialize a repository, practice branching, resolving merge conflicts, and tagging release versions.",
    },
    "github": {
        "course": "Introduction to Git and GitHub",
        "platform": "Coursera",
        "project": "Create an open-source repository with README, Issue templates, Pull Request workflow, and GitHub Pages.",
        "project_idea": "Create an open-source repository with README, Issue templates, Pull Request workflow, and GitHub Pages.",
    },
    "docker": {
        "course": "Docker for Beginners",
        "platform": "freeCodeCamp",
        "project": "Dockerize a Python Flask web app with a multi-stage Dockerfile and run it locally in a container.",
        "project_idea": "Dockerize a Python Flask web app with a multi-stage Dockerfile and run it locally in a container.",
    },
    "kubernetes": {
        "course": "Kubernetes Course for Beginners",
        "platform": "freeCodeCamp",
        "project": "Deploy a multi-pod web app on Minikube with a Deployment, Service, and ConfigMap.",
        "project_idea": "Deploy a multi-pod web app on Minikube with a Deployment, Service, and ConfigMap.",
    },
    "aws": {
        "course": "AWS Certified Cloud Practitioner Training",
        "platform": "freeCodeCamp",
        "project": "Deploy a static website to an AWS S3 bucket configured for public hosting with CloudFront distribution.",
        "project_idea": "Deploy a static website to an AWS S3 bucket configured for public hosting with CloudFront distribution.",
    },
    "azure": {
        "course": "Microsoft Azure Fundamentals (AZ-900)",
        "platform": "freeCodeCamp",
        "project": "Deploy a serverless Azure Function triggered by HTTP requests that processes incoming JSON payloads.",
        "project_idea": "Deploy a serverless Azure Function triggered by HTTP requests that processes incoming JSON payloads.",
    },
    "gcp": {
        "course": "Google Cloud Platform Fundamentals: Core Infrastructure",
        "platform": "Coursera",
        "project": "Deploy a containerized web app to Google Cloud Run and configure custom environment variables.",
        "project_idea": "Deploy a containerized web app to Google Cloud Run and configure custom environment variables.",
    },
    "linux": {
        "course": "Linux for Beginners",
        "platform": "freeCodeCamp",
        "project": "Write Bash shell scripts to automate daily file backups, log rotation, and system resource monitoring.",
        "project_idea": "Write Bash shell scripts to automate daily file backups, log rotation, and system resource monitoring.",
    },
    "terraform": {
        "course": "Terraform Course for Beginners",
        "platform": "freeCodeCamp",
        "project": "Write Infrastructure-as-Code to provision an AWS S3 bucket and IAM user with Terraform.",
        "project_idea": "Write Infrastructure-as-Code to provision an AWS S3 bucket and IAM user with Terraform.",
    },
    "jenkins": {
        "course": "Jenkins Tutorial for Beginners",
        "platform": "YouTube",
        "project": "Create a Jenkins Declarative Pipeline that pulls code from GitHub, runs automated unit tests, and archives artifacts.",
        "project_idea": "Create a Jenkins Declarative Pipeline that pulls code from GitHub, runs automated unit tests, and archives artifacts.",
    },
    "ci/cd": {
        "course": "GitHub Actions Full Course",
        "platform": "freeCodeCamp",
        "project": "Set up a CI/CD GitHub Actions workflow that runs linting, executes test suites, and builds releases on push.",
        "project_idea": "Set up a CI/CD GitHub Actions workflow that runs linting, executes test suites, and builds releases on push.",
    },

    # Data Science, ML & AI
    "machine learning": {
        "course": "Supervised Machine Learning: Regression and Classification",
        "platform": "Coursera",
        "project": "Train a house price prediction model using Linear Regression with feature scaling and cross-validation.",
        "project_idea": "Train a house price prediction model using Linear Regression with feature scaling and cross-validation.",
    },
    "deep learning": {
        "course": "Deep Learning Specialization",
        "platform": "Coursera",
        "project": "Build and train a multi-layer neural network from scratch to classify handwritten digits on the MNIST dataset.",
        "project_idea": "Build and train a multi-layer neural network from scratch to classify handwritten digits on the MNIST dataset.",
    },
    "artificial intelligence": {
        "course": "AI for Everyone",
        "platform": "Coursera",
        "project": "Develop an AI-powered game-playing bot using the Minimax algorithm for Tic-Tac-Toe.",
        "project_idea": "Develop an AI-powered game-playing bot using the Minimax algorithm for Tic-Tac-Toe.",
    },
    "natural language processing": {
        "course": "Natural Language Processing with Python",
        "platform": "freeCodeCamp",
        "project": "Build a customer feedback sentiment analysis tool using tokenization and TF-IDF classification.",
        "project_idea": "Build a customer feedback sentiment analysis tool using tokenization and TF-IDF classification.",
    },
    "computer vision": {
        "course": "OpenCV Course - Computer Vision with Python",
        "platform": "freeCodeCamp",
        "project": "Create a real-time face and eye detection application using OpenCV and webcam feed.",
        "project_idea": "Create a real-time face and eye detection application using OpenCV and webcam feed.",
    },
    "data analysis": {
        "course": "Data Analysis with Python Course",
        "platform": "freeCodeCamp",
        "project": "Perform exploratory data analysis on a real-world sales dataset to identify seasonal revenue trends.",
        "project_idea": "Perform exploratory data analysis on a real-world sales dataset to identify seasonal revenue trends.",
    },
    "pandas": {
        "course": "Pandas Full Course",
        "platform": "YouTube",
        "project": "Clean a messy real-estate dataset by handling missing values, filtering outliers, and grouping metrics.",
        "project_idea": "Clean a messy real-estate dataset by handling missing values, filtering outliers, and grouping metrics.",
    },
    "numpy": {
        "course": "NumPy Tutorial for Beginners",
        "platform": "freeCodeCamp",
        "project": "Implement basic linear algebra operations and matrix transformations for image filtering.",
        "project_idea": "Implement basic linear algebra operations and matrix transformations for image filtering.",
    },
    "scikit-learn": {
        "course": "Machine Learning with Python and Scikit-Learn",
        "platform": "freeCodeCamp",
        "project": "Build a churn prediction pipeline with feature encoders, Random Forest classifier, and ROC-AUC evaluation.",
        "project_idea": "Build a churn prediction pipeline with feature encoders, Random Forest classifier, and ROC-AUC evaluation.",
    },
    "tensorflow": {
        "course": "TensorFlow 2.0 Complete Course",
        "platform": "freeCodeCamp",
        "project": "Construct a Convolutional Neural Network (CNN) to classify images of clothing from Fashion MNIST.",
        "project_idea": "Construct a Convolutional Neural Network (CNN) to classify images of clothing from Fashion MNIST.",
    },
    "pytorch": {
        "course": "PyTorch for Deep Learning Bootcamp",
        "platform": "freeCodeCamp",
        "project": "Build and train a binary image classifier using PyTorch DataLoader, torchvision, and custom transfer learning.",
        "project_idea": "Build and train a binary image classifier using PyTorch DataLoader, torchvision, and custom transfer learning.",
    },

    # Business Intelligence & Analytics
    "excel": {
        "course": "Excel for Beginners",
        "platform": "YouTube",
        "project": "Create a dynamic monthly budget dashboard with VLOOKUP, pivot tables, and conditional formatting.",
        "project_idea": "Create a dynamic monthly budget dashboard with VLOOKUP, pivot tables, and conditional formatting.",
    },
    "power bi": {
        "course": "Power BI Full Course",
        "platform": "freeCodeCamp",
        "project": "Build an interactive retail sales performance dashboard with slicers, KPI cards, and trend charts.",
        "project_idea": "Build an interactive retail sales performance dashboard with slicers, KPI cards, and trend charts.",
    },
    "tableau": {
        "course": "Tableau for Beginners",
        "platform": "freeCodeCamp",
        "project": "Design an interactive global demographic story dashboard with map visualizations.",
        "project_idea": "Design an interactive global demographic story dashboard with map visualizations.",
    },

    # APIs & Architecture
    "rest api": {
        "course": "APIs for Beginners",
        "platform": "freeCodeCamp",
        "project": "Design and implement a RESTful recipe API with proper HTTP verbs, status codes, and query filtering.",
        "project_idea": "Design and implement a RESTful recipe API with proper HTTP verbs, status codes, and query filtering.",
    },
    "graphql": {
        "course": "GraphQL Full Course",
        "platform": "freeCodeCamp",
        "project": "Build a GraphQL server for a bookstore with schemas, queries, and mutations for authors and books.",
        "project_idea": "Build a GraphQL server for a bookstore with schemas, queries, and mutations for authors and books.",
    },

    # Methodologies & Soft Skills
    "agile": {
        "course": "Agile with Atlassian Jira",
        "platform": "Coursera",
        "project": "Set up a simulated product backlog, create user stories with acceptance criteria, and plan a 2-week sprint.",
        "project_idea": "Set up a simulated product backlog, create user stories with acceptance criteria, and plan a 2-week sprint.",
    },
    "scrum": {
        "course": "Scrum Master Certification Prep",
        "platform": "YouTube",
        "project": "Facilitate mock sprint ceremonies (sprint planning, daily standup, sprint review, retrospective) with team documentation.",
        "project_idea": "Facilitate mock sprint ceremonies (sprint planning, daily standup, sprint review, retrospective) with team documentation.",
    },
    "communication": {
        "course": "Improving Communication Skills",
        "platform": "Coursera",
        "project": "Draft an executive summary and a technical design document explaining a software project to non-technical stakeholders.",
        "project_idea": "Draft an executive summary and a technical design document explaining a software project to non-technical stakeholders.",
    },
    "problem solving": {
        "course": "Problem Solving through Programming in C",
        "platform": "NPTEL",
        "project": "Solve 20 beginner algorithm challenges on LeetCode/HackerRank and write step-by-step problem breakdown notes.",
        "project_idea": "Solve 20 beginner algorithm challenges on LeetCode/HackerRank and write step-by-step problem breakdown notes.",
    },
    "leadership": {
        "course": "Building Your Leadership Skills",
        "platform": "Coursera",
        "project": "Create a team mentorship framework including onboarding checklists, 1-on-1 agendas, and goal-tracking templates.",
        "project_idea": "Create a team mentorship framework including onboarding checklists, 1-on-1 agendas, and goal-tracking templates.",
    },
    "teamwork": {
        "course": "Teamwork Skills: Communicating Effectively in Groups",
        "platform": "Coursera",
        "project": "Contribute documentation and bug fixes to an open-source project following collaborative review guidelines.",
        "project_idea": "Contribute documentation and bug fixes to an open-source project following collaborative review guidelines.",
    },
    "project management": {
        "course": "Google Project Management Professional Certificate (Free Audit)",
        "platform": "Coursera",
        "project": "Develop a complete project charter, work breakdown structure (WBS), and risk management matrix for a software launch.",
        "project_idea": "Develop a complete project charter, work breakdown structure (WBS), and risk management matrix for a software launch.",
    },
}

# Aliases for flexibility and ease of import
SUGGESTIONS = SKILL_SUGGESTIONS
suggestions = SKILL_SUGGESTIONS


def get_suggestion(skill: str) -> Dict[str, str]:
    """Retrieve course and project suggestions for a given skill."""
    return SKILL_SUGGESTIONS.get(
        skill.strip().lower(),
        {
            "course": "Recommended Online Tutorial",
            "platform": "freeCodeCamp / YouTube",
            "project": f"Build a practical beginner project demonstrating practical usage of {skill}.",
            "project_idea": f"Build a practical beginner project demonstrating practical usage of {skill}.",
        },
    )


__all__ = ["SKILL_SUGGESTIONS", "SUGGESTIONS", "suggestions", "get_suggestion"]
