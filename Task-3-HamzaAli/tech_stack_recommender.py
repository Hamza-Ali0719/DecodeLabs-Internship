"""
Project 3: AI Recommendation Logic – Tech Stack Recommender
============================================================
Author      : Hamza Ali
Batch       : 2026
Institution : DecodeLabs
Description : A content-based recommendation system that matches
              user skills to job roles using TF-IDF vectorization
              and Cosine Similarity.
"""

import os
import sys
import logging
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ------------------------------------------------------------------
# LOGGING CONFIGURATION (Dual Channel: File + Console)
# ------------------------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(script_dir, "recommendation_log.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class TechStackRecommender:
    """
    A content-based recommendation engine that matches user skills
    to job roles using TF-IDF vectorization and Cosine Similarity.
    """

    def __init__(self, csv_path: str):
        """
        Initialize the recommender with the dataset path.

        Args:
            csv_path (str): Path to the CSV file containing skills and job roles.
        """
        self.csv_path = csv_path
        self.script_dir = os.path.dirname(os.path.abspath(csv_path))
        self.df = None
        self.job_roles = None
        self.skill_columns = None
        self.tfidf_matrix = None
        self.vectorizer = None
        logger.info(f"Recommender initialized with dataset: {csv_path}")

    def load_data(self) -> None:
        """
        Load the CSV dataset containing skills and job roles.
        Handles FileNotFoundError gracefully.
        """
        try:
            if not os.path.exists(self.csv_path):
                raise FileNotFoundError(f"Dataset not found: {self.csv_path}")

            self.df = pd.read_csv(self.csv_path)
            logger.info(f"Data loaded successfully. Shape: {self.df.shape}")

            # Display available job roles
            self.job_roles = self.df["Job_Role"].tolist()
            logger.info(f"Total job roles: {len(self.job_roles)}")

            # Identify skill columns (all columns except 'Job_Role')
            self.skill_columns = [col for col in self.df.columns if col != "Job_Role"]
            logger.info(f"Skill columns: {len(self.skill_columns)}")

            # Show sample data
            logger.info("\n" + "-" * 60)
            logger.info("SAMPLE DATA (First 3 rows):")
            logger.info("\n" + str(self.df.head(3)))
            logger.info("-" * 60)

        except FileNotFoundError as e:
            logger.error(f"File Error: {e}")
            sys.exit(1)
        except Exception as e:
            logger.error(f"Unexpected error while loading data: {e}")
            sys.exit(1)

    def preprocess_data(self) -> None:
        """
        Convert the skill matrix into a single text column for TF-IDF processing.
        Each row becomes a space-separated string of skills.
        """
        logger.info("Starting preprocessing...")

        # Convert each row to a skill string
        self.df["Skills_String"] = self.df[self.skill_columns].apply(
            lambda row: " ".join(row.astype(str)), axis=1
        )

        logger.info(f"Created Skills_String column. Sample:")
        logger.info(f"  {self.df['Skills_String'].iloc[0][:100]}...")
        logger.info("Preprocessing complete.")

    def vectorize_data(self) -> None:
        """
        Apply TF-IDF vectorization to convert skill strings into numerical vectors.
        """
        logger.info("Starting TF-IDF vectorization...")

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            max_features=100
        )

        self.tfidf_matrix = self.vectorizer.fit_transform(self.df["Skills_String"])
        logger.info(f"TF-IDF matrix shape: {self.tfidf_matrix.shape}")
        logger.info(f"Vocabulary size: {len(self.vectorizer.get_feature_names_out())}")

        # Log top features
        feature_names = self.vectorizer.get_feature_names_out()
        logger.info(f"Sample features: {list(feature_names[:10])}")
        logger.info("Vectorization complete.")

    def get_user_skills(self) -> list:
        """
        Prompt the user to enter their skills (minimum 3).
        Returns a list of skills.
        """
        logger.info("\n" + "=" * 60)
        logger.info("USER SKILLS INPUT")
        logger.info("=" * 60)

        print("\n" + "=" * 60)
        print("TECH STACK RECOMMENDER - Find Your Ideal Job Role")
        print("=" * 60)
        print("\nEnter your skills (minimum 3). Press Enter after each skill.")
        print("Type 'done' when finished.\n")

        skills = []
        while len(skills) < 3:
            skill = input(f"Skill {len(skills) + 1}: ").strip().title()
            if skill.lower() == "done":
                if len(skills) < 3:
                    print(f"You need at least 3 skills. Currently: {len(skills)}")
                    continue
                break
            if skill:
                skills.append(skill)
                logger.info(f"User added skill: {skill}")
            else:
                print("Please enter a valid skill.")

        logger.info(f"User skills collected: {skills}")
        return skills

    def create_user_vector(self, skills: list) -> np.ndarray:
        """
        Convert user skills into a TF-IDF vector using the pre-fitted vectorizer.

        Args:
            skills (list): List of user skills.

        Returns:
            np.ndarray: TF-IDF vector representation of user skills.
        """
        # Join skills into a space-separated string
        skills_string = " ".join(skills)
        user_vector = self.vectorizer.transform([skills_string])
        return user_vector

    def calculate_similarity(self, user_vector: np.ndarray) -> np.ndarray:
        """
        Calculate cosine similarity between user vector and all job role vectors.

        Args:
            user_vector (np.ndarray): TF-IDF vector of user skills.

        Returns:
            np.ndarray: Similarity scores for each job role.
        """
        similarities = cosine_similarity(user_vector, self.tfidf_matrix).flatten()
        logger.info(f"Similarity scores calculated for {len(similarities)} roles.")
        return similarities

    def get_top_recommendations(self, similarities: np.ndarray, top_n: int = 3) -> pd.DataFrame:
        """
        Sort job roles by similarity and return the top N recommendations.

        Args:
            similarities (np.ndarray): Similarity scores for each role.
            top_n (int): Number of top recommendations to return.

        Returns:
            pd.DataFrame: Top N job roles with their similarity scores.
        """
        # Create a DataFrame with job roles and scores
        results = pd.DataFrame({
            "Job_Role": self.job_roles,
            "Similarity_Score": similarities
        })

        # Sort by similarity (descending)
        results = results.sort_values("Similarity_Score", ascending=False)

        # Return top N
        top_results = results.head(top_n)
        return top_results

    def display_recommendations(self, top_results: pd.DataFrame) -> None:
        """
        Display the recommendations in a clean, user-friendly format.

        Args:
            top_results (pd.DataFrame): Top N job roles with scores.
        """
        print("\n" + "=" * 60)
        print("🌟 YOUR TOP RECOMMENDATIONS 🌟")
        print("=" * 60)

        for idx, row in top_results.iterrows():
            score_percent = row["Similarity_Score"] * 100
            print(f"\n📌 {row['Job_Role']}")
            print(f"   Match Score: {score_percent:.1f}%")

            # Add a visual progress bar
            bar_length = int(score_percent / 5)  # Max 20 bars
            bar = "█" * bar_length + "░" * (20 - bar_length)
            print(f"   [ {bar} ]")

        print("\n" + "=" * 60)

        # Save results to file
        self._save_results(top_results)

    def _save_results(self, results: pd.DataFrame) -> None:
        """
        Save the recommendations to a text file.

        Args:
            results (pd.DataFrame): Top N job roles with scores.
        """
        try:
            file_path = os.path.join(self.script_dir, "recommendation_results.txt")
            with open(file_path, "w") as f:
                f.write("=" * 60 + "\n")
                f.write("TECH STACK RECOMMENDER - RESULTS\n")
                f.write("=" * 60 + "\n\n")
                f.write(results.to_string(index=False))
                f.write("\n\n" + "=" * 60 + "\n")
            logger.info(f"Results saved to '{file_path}'")
        except Exception as e:
            logger.error(f"Could not save results: {e}")

    def run_pipeline(self) -> None:
        """
        Execute the complete recommendation pipeline.
        """
        logger.info("\n" + "=" * 60)
        logger.info("STARTING RECOMMENDATION PIPELINE")
        logger.info("=" * 60)

        # Step 1: Load and preprocess data
        self.load_data()
        self.preprocess_data()
        self.vectorize_data()

        # Step 2: Get user input
        user_skills = self.get_user_skills()

        # Step 3: Create user vector and calculate similarity
        user_vector = self.create_user_vector(user_skills)
        similarities = self.calculate_similarity(user_vector)

        # Step 4: Get and display recommendations
        top_results = self.get_top_recommendations(similarities, top_n=3)
        self.display_recommendations(top_results)

        logger.info("\n" + "=" * 60)
        logger.info("RECOMMENDATION PIPELINE COMPLETED SUCCESSFULLY.")
        logger.info("Check 'recommendation_log.log' and 'recommendation_results.txt'")
        logger.info("=" * 60)


if __name__ == "__main__":
    # Script Entry Point
    # Dynamically locate the CSV file in the same folder as this script.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, "raw_skills.csv")

    # Instantiate and run the recommender
    recommender = TechStackRecommender(csv_path=csv_file)
    recommender.run_pipeline()
