"""
Project 2: E-Commerce Order Status Classification
==================================================
Author      : Hamza Ali
Batch       : 2026
Institution : DecodeLabs
Description : A professional machine learning pipeline that predicts 
              Order Status (Cancelled/Returned/Pending/Shipped/Delivered)
              using Logistic Regression. Includes logging, visualization,
              and feature importance analysis.
"""

import os
import sys
import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# ------------------------------------------------------------------
# LOGGING CONFIGURATION (Dual Channel: File + Console)
# ------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("classification.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class OrderStatusClassifier:
    """
    A complete ML pipeline to classify e-commerce order status.
    Encapsulates loading, preprocessing, training, and evaluation.
    """

    def __init__(self, file_path: str, target_col: str = "OrderStatus"):
        """
        Initialize the classifier with the dataset path and target column.

        Args:
            file_path (str): Path to the Excel file.
            target_col (str): Name of the target column to predict.
        """
        self.file_path = file_path
        self.target_col = target_col
        self.df = None
        self.X = None
        self.y = None
        self.X_train_scaled = None
        self.X_test_scaled = None
        self.y_train = None
        self.y_test = None
        self.model = None
        self.scaler = StandardScaler()
        self.target_encoder = LabelEncoder()
        self.encoders = {}
        self.feature_names = None
        logger.info(f"Classifier initialized with file: {file_path}")

    def load_data(self) -> None:
        """
        Load the Excel dataset from the specified path.
        Handles FileNotFoundError and invalid Excel formats gracefully.
        """
        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"File not found: {self.file_path}")

            self.df = pd.read_excel(self.file_path)
            logger.info(f"Data loaded successfully. Shape: {self.df.shape}")

            # Print initial distribution of the target
            logger.info("\n" + "-" * 50)
            logger.info("TARGET VARIABLE DISTRIBUTION:")
            logger.info("\n" + str(self.df[self.target_col].value_counts()))
            logger.info("-" * 50)

        except FileNotFoundError as e:
            logger.error(f"File Error: {e}")
            sys.exit(1)
        except Exception as e:
            logger.error(f"Unexpected error while loading data: {e}")
            sys.exit(1)

    def preprocess(self) -> None:
        """
        Clean and prepare the data for training.
        - Drops unique identifiers (ID, Address, Tracking, etc.) to prevent data leakage.
        - Fills missing CouponCode values.
        - Separates features (X) and target (y).
        """
        logger.info("Starting preprocessing...")

        # Drop columns that are unique per row (no predictive signal)
        drop_cols = ["OrderID", "CustomerID", "ShippingAddress", "TrackingNumber", "Date"]
        # Keep only columns that exist in the dataframe
        drop_cols = [col for col in drop_cols if col in self.df.columns]

        data = self.df.drop(columns=drop_cols, errors="ignore")
        logger.info(f"Dropped columns: {drop_cols}")

        # Fill missing coupon codes with a placeholder
        if "CouponCode" in data.columns:
            data["CouponCode"] = data["CouponCode"].fillna("NoCoupon")
            logger.info("Filled missing CouponCode with 'NoCoupon'.")

        # Separate features and target
        self.X = data.drop(columns=[self.target_col])
        self.y = data[self.target_col]
        self.feature_names = self.X.columns.tolist()

        logger.info(f"Features: {len(self.feature_names)} columns")
        logger.info(f"Target: {self.target_col}")
        logger.info("Preprocessing complete.")

    def encode_features(self) -> None:
        """
        Convert all categorical text columns into numeric values using LabelEncoder.
        Also encodes the target variable (y).
        """
        logger.info("Starting feature encoding...")

        # Select categorical columns (text/string type)
        categorical_cols = self.X.select_dtypes(include=["object", "string"]).columns.tolist()

        for col in categorical_cols:
            le = LabelEncoder()
            self.X[col] = le.fit_transform(self.X[col].astype(str))
            self.encoders[col] = le
            logger.debug(f"Encoded column: {col}")

        # Encode the target variable
        self.y_encoded = self.target_encoder.fit_transform(self.y)
        logger.info(f"Target encoded. Classes: {self.target_encoder.classes_}")

        # Replace y with encoded values for consistent use
        self.y = self.y_encoded
        logger.info("Encoding complete.")

    def split_data(self, test_size: float = 0.2, random_state: int = 42) -> None:
        """
        Split the data into training and testing sets.
        Uses stratification to maintain class distribution in both sets.
        """
        logger.info(f"Splitting data into train/test (test_size={test_size})...")
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X,
            self.y,
            test_size=test_size,
            random_state=random_state,
            stratify=self.y
        )
        logger.info(f"Train size: {len(self.X_train)} rows")
        logger.info(f"Test size: {len(self.X_test)} rows")

    def scale_features(self) -> None:
        """
        Standardize numeric features to mean=0, std=1.
        Prevents features with large numbers (e.g., UnitPrice) from dominating the model.
        """
        logger.info("Scaling numeric features...")
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        logger.info("Scaling complete.")

    def train_model(self) -> None:
        """
        Train a Logistic Regression model on the scaled training data.
        """
        logger.info("Training Logistic Regression model...")
        self.model = LogisticRegression(max_iter=1000, random_state=42)
        self.model.fit(self.X_train_scaled, self.y_train)
        logger.info("Model training complete.")

    def evaluate(self) -> dict:
        """
        Evaluate the trained model on the test set.
        Prints Accuracy, Classification Report, and Confusion Matrix.
        Also calculates baseline accuracy (guessing the majority class).

        Returns:
            dict: A dictionary containing accuracy, classification report, and confusion matrix.
        """
        logger.info("Evaluating model performance...")
        y_pred = self.model.predict(self.X_test_scaled)

        # Metrics
        acc = accuracy_score(self.y_test, y_pred)
        report = classification_report(
            self.y_test,
            y_pred,
            target_names=self.target_encoder.classes_,
            output_dict=True
        )
        report_str = classification_report(
            self.y_test,
            y_pred,
            target_names=self.target_encoder.classes_
        )
        conf_matrix = confusion_matrix(self.y_test, y_pred)

        # Baseline: what if we just guessed the most common class every time?
        baseline_acc = pd.Series(self.y_train).value_counts(normalize=True).max()

        # Print results
        logger.info("-" * 60)
        logger.info(f"🔹 MODEL ACCURACY: {acc:.3f} ({acc*100:.1f}%)")
        logger.info(f"🔹 BASELINE ACCURACY (Guess Majority Class): {baseline_acc:.3f} ({baseline_acc*100:.1f}%)")
        logger.info("-" * 60)
        logger.info("\nCLASSIFICATION REPORT:\n")
        logger.info(report_str)
        logger.info("\nCONFUSION MATRIX:")
        logger.info("\n" + str(conf_matrix))

        # Professional Interpretation
        if acc < baseline_acc:
            logger.warning("⚠️  MODEL UNDERPERFORMS BASELINE.")
            logger.warning("This typically means the features have no predictive relationship with the target.")
            logger.warning("It is NOT a coding error; it indicates the dataset is likely random/synthetic in nature.")
        else:
            logger.info("✅ Model outperforms the baseline. Features have predictive power.")

        # Store results for later use
        self.results = {
            "accuracy": acc,
            "baseline": baseline_acc,
            "report": report,
            "confusion_matrix": conf_matrix,
            "y_pred": y_pred
        }

        # Save the report to a text file
        self._save_report_to_file(report_str, acc, baseline_acc)
        # Plot the confusion matrix
        self._plot_confusion_matrix(conf_matrix)

        return self.results

    def _save_report_to_file(self, report_str: str, acc: float, baseline: float) -> None:
        """Save evaluation metrics to a results.txt file for record-keeping."""
        try:
            with open("classification_results.txt", "w") as f:
                f.write("=" * 60 + "\n")
                f.write("CLASSIFICATION RESULTS\n")
                f.write(f"Accuracy: {acc:.3f}\n")
                f.write(f"Baseline (majority guess): {baseline:.3f}\n")
                f.write("=" * 60 + "\n\n")
                f.write(report_str)
                f.write("\n\nConfusion Matrix:\n")
                f.write(str(self.results["confusion_matrix"]))
            logger.info("Results saved to 'classification_results.txt'")
        except Exception as e:
            logger.error(f"Could not save results file: {e}")

    def _plot_confusion_matrix(self, conf_matrix: np.ndarray) -> None:
        """Generate and save a heatmap of the confusion matrix."""
        try:
            plt.figure(figsize=(8, 6))
            sns.heatmap(
                conf_matrix,
                annot=True,
                fmt="d",
                cmap="Blues",
                xticklabels=self.target_encoder.classes_,
                yticklabels=self.target_encoder.classes_
            )
            plt.title("Confusion Matrix - Order Status Classification")
            plt.ylabel("Actual")
            plt.xlabel("Predicted")
            plt.tight_layout()
            plt.savefig("confusion_matrix.png", dpi=300)
            logger.info("Confusion matrix plot saved to 'confusion_matrix.png'")
            # Close the plot to free memory
            plt.close()
        except ImportError:
            logger.warning("Matplotlib or Seaborn not fully installed. Skipping plot generation.")
        except Exception as e:
            logger.error(f"Could not generate confusion matrix plot: {e}")

    def analyze_feature_importance(self) -> None:
        """
        Analyze and display the top positive/negative features influencing the model.
        Helps in understanding what drives the decision for specific classes.
        """
        if self.model is None:
            logger.error("Model not trained. Cannot analyze features.")
            return

        logger.info("-" * 60)
        logger.info("FEATURE IMPORTANCE ANALYSIS (Coefficients)")
        logger.info("-" * 60)

        # Logistic Regression gives us coefficients per class
        coefficients = self.model.coef_
        class_names = self.target_encoder.classes_

        for i, class_name in enumerate(class_names):
            # Sort features by coefficient magnitude (importance) for this class
            coefs = coefficients[i]
            # Get top 5 positive (push toward this class) and negative (push away)
            top_positive_idx = np.argsort(coefs)[-5:][::-1]
            top_negative_idx = np.argsort(coefs)[:5]

            logger.info(f"\n🔹 Class: {class_name}")
            logger.info("  Top 5 Features INCREASING probability:")
            for idx in top_positive_idx:
                logger.info(f"    + {self.feature_names[idx]}: {coefs[idx]:.3f}")

            logger.info("  Top 5 Features DECREASING probability:")
            for idx in top_negative_idx:
                logger.info(f"    - {self.feature_names[idx]}: {coefs[idx]:.3f}")

        logger.info("-" * 60)

    def run_pipeline(self) -> None:
        """
        Execute the entire classification pipeline in order.
        """
        logger.info("\n" + "=" * 60)
        logger.info("STARTING CLASSIFICATION PIPELINE")
        logger.info("=" * 60)

        self.load_data()
        self.preprocess()
        self.encode_features()
        self.split_data()
        self.scale_features()
        self.train_model()
        self.evaluate()
        self.analyze_feature_importance()

        logger.info("\n" + "=" * 60)
        logger.info("CLASSIFICATION PIPELINE COMPLETED SUCCESSFULLY.")
        logger.info("Check 'classification.log', 'classification_results.txt', and 'confusion_matrix.png'")
        logger.info("=" * 60)


if __name__ == "__main__":
    # Script Entry Point
    # Dynamically locate the Excel file in the same folder as this script.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    excel_file = os.path.join(script_dir, "Dataset_for_Data_Analytics.xlsx")

    # Instantiate and run the classifier
    classifier = OrderStatusClassifier(file_path=excel_file)
    classifier.run_pipeline()
