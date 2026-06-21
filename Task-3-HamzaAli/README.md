🚀 Tech Stack Recommender

<p align="center"> <b>AI-Powered Job Role Recommendation System using TF-IDF & Cosine Similarity</b> </p> <p align="center"> <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python"> <img src="https://img.shields.io/badge/ML-TF--IDF-orange"> <img src="https://img.shields.io/badge/Algorithm-Cosine%20Similarity-green"> <img src="https://img.shields.io/badge/Status-Completed-success"> <img src="https://img.shields.io/badge/License-MIT-lightgrey"> </p>
📌 Overview

The Tech Stack Recommender is an AI-based system that suggests the most relevant job roles based on user-provided skills.

It uses:

📊 TF-IDF Vectorization (Text → Numbers)
📐 Cosine Similarity (Matching algorithm)
🧠 Content-Based Filtering (No user history required)

👉 Example:

Input: Python, Cloud, Automation
Output: Cloud Architect, DevOps Engineer, SRE

🎯 Features
✔️ AI-based job role recommendations
✔️ TF-IDF text vectorization
✔️ Cosine similarity scoring
✔️ Top-3 ranked results
✔️ Progress bar visualization
✔️ Input validation (minimum 3 skills required)
✔️ Logging system (console + file)
✔️ Results saved to .txt file
🧠 How It Works
User Skills → TF-IDF Vector → Cosine Similarity → Ranking → Top Jobs
🔄 Pipeline
User enters skills
Skills are converted into text vector
Dataset is vectorized using TF-IDF
Similarity is calculated
Top matching job roles are returned
🏗️ Project Structure
Tech-Stack-Recommender/
│
├── tech_stack_recommender.py     # Main AI system
├── raw_skills.csv                # Dataset (skills → roles)
├── recommendation_log.log       # Logs (auto-generated)
├── recommendation_results.txt   # Output file
├── README.md                    # Documentation
└── screenshots/                 # Output images
⚙️ Tech Stack
Technology	Purpose
Python	Core programming
Pandas	Data handling
NumPy	Numerical operations
Scikit-learn	ML algorithms (TF-IDF, Cosine Similarity)
Logging	Tracking execution
🚀 Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/Tech-Stack-Recommender.git
cd Tech-Stack-Recommender
2️⃣ Install Dependencies
pip install pandas numpy scikit-learn
3️⃣ Run Project
python tech_stack_recommender.py
🧪 Example Usage
Input:
Python
Cloud
Automation
Output:
📌 Cloud Architect
Match Score: 78.3%

📌 DevOps Engineer
Match Score: 72.1%

📌 Site Reliability Engineer
Match Score: 65.8%
📊 Algorithm Explanation
🔹 TF-IDF

Converts text into weighted vectors:

Rare skills → higher importance
Common words → lower weight
🔹 Cosine Similarity

Measures angle between vectors:

1.0 → Perfect match
0.0 → No similarity
📈 System Architecture
Input (User Skills)
        ↓
TF-IDF Vectorization
        ↓
Similarity Calculation
        ↓
Ranking Engine
        ↓
Top-N Results
🧪 Testing
Test Case	Result
Valid skills input	✅ Passed
Less than 3 skills	❌ Rejected
Mixed case input	✅ Handled
Unknown skills	⚠️ Best-effort match
🚧 Challenges & Solutions
Challenge	Solution
Input validation	Minimum 3 skills enforced
Case sensitivity	lowercase normalization
Sparse dataset	TF-IDF optimization
Logging issues	Fixed file path handling
🔮 Future Improvements
🌐 Web UI (Streamlit / Flask)
🤝 Hybrid recommendation system
📡 Real job market API integration
🧠 Skill weighting system
📊 Dashboard analytics
📜 Conclusion

This project demonstrates a real-world AI recommendation system using NLP techniques. It simulates how platforms like LinkedIn, Netflix, and Amazon recommend content based on similarity rather than user history.

👨‍💻 Author

Hamza Ali
📍 Decode Labs Internship Project
📅 June 2026

📎 License

This project is for educational purposes.
