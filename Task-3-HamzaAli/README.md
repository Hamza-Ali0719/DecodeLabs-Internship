# 🎯 Tech Stack Recommender – AI Recommendation Logic

> **DecodeLabs** | Project 3 | Batch 2026

| **Submitted By** | Hamza Ali |
| :--- | :--- |
| **Category** | Internship |
| **Course / Subject** | Artificial Intelligence Project 3 |
| **Department** | Computer Science |
| **Institution** | Decode Labs |
| **Submission Date** | June 2026 |
| **Project Repository** | [https://github.com/Hamza-Ali0719/DecodeLabs-Internship](https://github.com/Hamza-Ali0719/DecodeLabs-Internship) |

---

## 📚 Table of Contents

- [1. Introduction](#1-introduction)
- [2. Objectives](#2-objectives)
- [3. Tools & Technologies Used](#3-tools--technologies-used)
- [4. System Architecture](#4-system-architecture)
  - [4.1 Component Overview](#41-component-overview)
- [5. Project Structure](#5-project-structure)
- [6. Code Walkthrough](#6-code-walkthrough)
  - [6.1 The `TechStackRecommender` Class](#61-the-techstackrecommender-class)
  - [6.2 Data Loading & Preprocessing](#62-data-loading--preprocessing)
  - [6.3 TF-IDF Vectorization](#63-tf-idf-vectorization)
  - [6.4 User Input Collection](#64-user-input-collection)
  - [6.5 Cosine Similarity Calculation](#65-cosine-similarity-calculation)
  - [6.6 Top-N Filtering & Display](#66-top-n-filtering--display)
- [7. Features Implemented](#7-features-implemented)
- [8. Sample Execution & Output](#8-sample-execution--output)
  - [8.1 Console Output](#81-console-output)
- [9. Testing & Validation](#9-testing--validation)
- [10. Challenges Faced and Solutions](#10-challenges-faced-and-solutions)
- [11. Future Enhancements](#11-future-enhancements)
- [12. Conclusion](#12-conclusion)
- [13. References](#13-references)
- [Appendix A: Full Source Code (tech_stack_recommender.py)](#appendix-a-full-source-code-tech_stack_recommenderpy)

---

## 1. Introduction

In the modern digital age, users are overwhelmed with choice. Recommendation systems serve as **digital matchmakers**, connecting users to relevant content before they even articulate their needs. From Netflix suggesting movies to Amazon recommending products, these systems drive engagement, retention, and commercial value.

This project, the **third milestone in my DecodeLabs internship**, implements a **Content-Based Recommendation System** using **TF-IDF** (Term Frequency-Inverse Document Frequency) and **Cosine Similarity**. Unlike Project 1 (Rule-Based Logic) and Project 2 (Classification), Project 3 introduces **similarity-based matching** – the engine behind modern AI recommendation systems.

The application, **Tech Stack Recommender**, takes user skills as input (e.g., `["Python", "Cloud", "Automation"]`) and recommends the **Top 3 most relevant job roles** (e.g., "Cloud Architect", "DevOps Engineer") based on skill alignment. This is achieved through:
- **Vectorization**: Converting text skills into numerical vectors using TF-IDF.
- **Similarity Scoring**: Measuring angular alignment using Cosine Similarity.
- **Ranking & Filtering**: Sorting results and displaying the top matches.

---

## 2. Objectives

- To design and implement a **content-based recommendation system** using TF-IDF vectorization and Cosine Similarity.
- To preprocess a structured dataset of skills mapped to job roles.
- To collect user input (minimum 3 skills) and transform it into a weighted vector.
- To calculate similarity scores between user profiles and all available job roles.
- To filter and display the **Top 3 most relevant job roles** with percentage match scores.
- To follow professional software engineering principles: Object-Oriented Programming (OOP), dual-channel logging, error handling, and result persistence.
- To produce a clean, user-friendly interface with visual progress bars for match scores.

---

## 3. Tools & Technologies Used

| Tool / Module | Purpose |
| :--- | :--- |
| **Python 3.9+** | Core programming language. |
| **Pandas** | Loading and manipulating the CSV dataset (DataFrames). |
| **NumPy** | Numerical operations and array handling. |
| **Scikit-learn (sklearn)** | TF-IDF vectorization (`TfidfVectorizer`) and Cosine Similarity (`cosine_similarity`). |
| **Logging** | Recording each pipeline step and results to a file and console. |
| **OS / Sys** | Dynamic file path handling and graceful exit on critical errors. |
| **Git / GitHub** | Version control and submission. |

---

## 4. System Architecture

The architecture follows the **IPO (Input-Process-Output)** model:

1. **Input** – User provides skills via console input (minimum 3 skills).
2. **Process** – TF-IDF vectorization transforms skills into numerical vectors; Cosine Similarity calculates alignment with job roles.
3. **Output** – Top 3 job roles are displayed with percentage match scores and visual progress bars.

### 4.1 Component Overview

| Component (Method) | Responsibility |
| :--- | :--- |
| `TechStackRecommender` | Main class encapsulating the entire recommendation pipeline. |
| `load_data()` | Reads CSV, handles file-not-found errors, displays sample data. |
| `preprocess_data()` | Converts skill columns into a single `Skills_String` column. |
| `vectorize_data()` | Applies TF-IDF vectorization to the skill strings. |
| `get_user_skills()` | Collects a minimum of 3 skills from the user via console input. |
| `create_user_vector()` | Transforms user skills into a TF-IDF vector. |
| `calculate_similarity()` | Computes Cosine Similarity between user vector and all job role vectors. |
| `get_top_recommendations()` | Sorts results and returns the Top N matches. |
| `display_recommendations()` | Prints recommendations with visual progress bars and saves results to a file. |
| `run_pipeline()` | The master orchestrator that calls all methods in sequence. |

---

## 5. Project Structure

```text
Task-3-HamzaAli/
├── tech_stack_recommender.py      # Main application code
├── raw_skills.csv                 # Dataset (skills → job roles)
├── README.md                      # Project documentation (this file)
├── recommendation_log.log         # Generated log file (auto-created)
├── recommendation_results.txt     # Saved results (auto-created)
└── (Screenshots)                  # Visual proof of execution
6. Code Walkthrough
This section breaks down the upgraded code (tech_stack_recommender.py) in detail.

6.1 The TechStackRecommender Class
The code is wrapped in a Python class for reusability and modularity. Key attributes include:

self.df – The dataset loaded from CSV.

self.job_roles – List of all job roles.

self.tfidf_matrix – The TF-IDF weighted matrix.

self.vectorizer – The fitted TF-IDF vectorizer.

6.2 Data Loading & Preprocessing
The load_data() method reads the CSV and identifies skill columns (all columns except Job_Role). The preprocess_data() method creates a Skills_String column by joining all skill values into a space-separated string.

6.3 TF-IDF Vectorization
The vectorize_data() method applies TfidfVectorizer with:

lowercase=True – Ensures case-insensitive matching.

stop_words="english" – Removes common English stop words.

max_features=100 – Limits vocabulary to the top 100 terms for efficiency.

6.4 User Input Collection
The get_user_skills() method prompts the user for skills (minimum 3). It validates input and logs each skill.

6.5 Cosine Similarity Calculation
The calculate_similarity() method uses cosine_similarity from scikit-learn to compute the angular alignment between the user vector and all job role vectors.

6.6 Top-N Filtering & Display
The get_top_recommendations() method sorts job roles by similarity score and returns the top N. The display_recommendations() method prints results with a visual progress bar (█░) for each recommendation and saves results to a text file.

7. Features Implemented
Feature	Description
Content-Based Filtering	Recommendations based on item attributes (skills), independent of other users.
TF-IDF Vectorization	Converts text skills into weighted numerical vectors, penalizing common terms.
Cosine Similarity	Measures angular alignment between user skills and job roles, invariant to vector magnitude.
User Input Validation	Ensures a minimum of 3 skills are provided before proceeding.
Top-N Filtering	Returns the top 3 most relevant job roles to prevent choice overload.
Visual Progress Bars	Displays match scores as visual bars (█░░░░) for intuitive understanding.
Dual-Channel Logging	All actions and metrics are logged to both console and recommendation_log.log.
Result Persistence	Saves recommendations to recommendation_results.txt for record-keeping.
Robust Error Handling	Gracefully handles missing files and invalid inputs without crashing.
8. Sample Execution & Output
8.1 Console Output
text
============================================================
TECH STACK RECOMMENDER - Find Your Ideal Job Role
============================================================

Enter your skills (minimum 3). Press Enter after each skill.
Type 'done' when finished.

Skill 1: Python
Skill 2: Cloud
Skill 3: Automation
Skill 4: done

============================================================
🌟 YOUR TOP RECOMMENDATIONS 🌟
============================================================

📌 Cloud Architect
   Match Score: 78.3%
   [ ████████████████░░░░ ]

📌 DevOps Engineer
   Match Score: 72.1%
   [ ██████████████░░░░░░ ]

📌 Site Reliability Engineer
   Match Score: 65.8%
   [ █████████████░░░░░░░ ]

============================================================
9. Testing & Validation
Test Case	Input	Expected Output	Result
Valid Skills	Python, Cloud, Automation	Top 3 roles (Cloud Architect, DevOps, SRE)	✅ Passed
Single Skill	Python only	Error: Need at least 3 skills	✅ Passed
Empty Input	Press Enter without typing	Error: Invalid skill	✅ Passed
Mixed Case	python, CLOUD, automation	Matched correctly (case-insensitive)	✅ Passed
Unknown Skills	Rust, Swift, Kotlin	Falls back to closest matches	✅ Passed
10. Challenges Faced and Solutions
Challenge	Solution Applied
User Input Validation	Implemented a while loop that ensures at least 3 valid skills are collected.
Cold Start Problem	Bypassed by requiring user input (onboarding survey) to build the initial profile.
Feature Alignment	Ensured user skills and job role skills use the same vocabulary via TF-IDF vectorizer.
Case Sensitivity	Used lowercase=True in TfidfVectorizer to make matching case-insensitive.
Logging File Location	Added script_dir to save logs in the project folder instead of the VS Code directory.
11. Future Enhancements
Collaborative Filtering – Integrate user-user similarity to recommend roles based on peers with similar skills.

Hybrid System – Combine content-based and collaborative filtering for more robust recommendations.

Web Interface – Build a Flask/Streamlit frontend for a more interactive user experience.

Real-world Data – Use live job market data (e.g., from LinkedIn or Indeed) to update skill mappings dynamically.

Skill Weighting – Allow users to rate the importance of each skill (e.g., "Expert", "Intermediate", "Beginner").

12. Conclusion
The Tech Stack Recommender successfully demonstrates the complete lifecycle of a content-based recommendation system: data loading, preprocessing, vectorization, similarity scoring, ranking, and display. While the model uses a simplified dataset, the underlying principles (TF-IDF, Cosine Similarity, Top-N filtering) are the same ones powering commercial systems like Netflix, Amazon, and Spotify.

This project proves my ability to build intelligent systems that bridge the gap between user intent and relevant content – a critical skill for any AI Engineer.

13. References
Pedregosa et al., "Scikit-learn: Machine Learning in Python," JMLR 12, pp. 2825-2830, 2011.

Python Software Foundation. "logging — Logging facility for Python."

"Content-Based Recommendation Systems," Towards Data Science.

Appendix A: Full Source Code (tech_stack_recommender.py)
