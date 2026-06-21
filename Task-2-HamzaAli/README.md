# 📊 E-Commerce Order Status Classification – A Machine Learning Pipeline

> **DecodeLabs** | Project 2 | Batch 2026

| **Submitted By** | Hamza Ali |
| :--- | :--- |
| **Category** | Internship |
| **Course / Subject** | Artificial Intelligence Project 2 |
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
  - [6.1 The `OrderStatusClassifier` Class](#61-the-orderstatusclassifier-class)
  - [6.2 Data Loading & Error Handling](#62-data-loading--error-handling)
  - [6.3 Preprocessing & Feature Selection](#63-preprocessing--feature-selection)
  - [6.4 Encoding & Train/Test Split](#64-encoding--traintest-split)
  - [6.5 Feature Scaling](#65-feature-scaling)
  - [6.6 Model Training](#66-model-training)
  - [6.7 Evaluation & Baseline Comparison](#67-evaluation--baseline-comparison)
  - [6.8 Feature Importance Analysis](#68-feature-importance-analysis)
- [7. Features Implemented](#7-features-implemented)
- [8. Sample Execution & Output](#8-sample-execution--output)
  - [8.1 Console Output](#81-console-output)
  - [8.2 Visual Output – Confusion Matrix](#82-visual-output--confusion-matrix)
- [9. Testing & Validation](#9-testing--validation)
  - [9.1 Handling Synthetic Data](#91-handling-synthetic-data)
- [10. Challenges Faced and Solutions](#10-challenges-faced-and-solutions)
- [11. Future Enhancements](#11-future-enhancements)
- [12. Conclusion](#12-conclusion)
- [13. References](#13-references)
- [Appendix A: Full Source Code (classify_order_status.py)](#appendix-a-full-source-code-classify_order_statuspy)

---

## 1. Introduction

Predicting order status (whether an order will be Cancelled, Returned, Pending, Shipped, or Delivered) is a critical task for e-commerce businesses. Accurate predictions help optimize inventory management, customer service, and logistics. 

This project, the **second milestone in my DecodeLabs internship**, implements a full end-to-end **Machine Learning classification pipeline** using Python. Unlike Project 1, which used deterministic `if-else` logic, Project 2 introduces probabilistic machine learning – specifically, **Logistic Regression**. 

The pipeline is designed with professional software engineering principles: Object-Oriented Programming (OOP), dual-channel logging, error handling, automated visualization, and baseline comparison. It predicts the `OrderStatus` from features such as product type, quantity, unit price, payment method, and referral source.

---

## 2. Objectives

- To design and implement a reusable, object-oriented machine learning pipeline for multi-class classification.
- To preprocess a real-world (synthetic) dataset, including cleaning, encoding, and feature scaling.
- To apply **Logistic Regression** to predict categorical outcomes with high interpretability.
- To evaluate model performance using multiple metrics (Accuracy, Classification Report, Confusion Matrix) and compare against a **Baseline** (always guessing the most common class).
- To analyze feature importance to understand which attributes influence order status decisions.
- To produce professional artifacts: structured logs, a saved classification report (`.txt`), and a visual Confusion Matrix heatmap (`.png`).

---

## 3. Tools & Technologies Used

The project uses a mix of core Python libraries for data science, with an emphasis on the `scikit-learn` ecosystem:

| Tool / Module | Purpose |
| :--- | :--- |
| **Python 3.9+** | Core programming language. |
| **Pandas** | Loading and manipulating the Excel dataset (DataFrames). |
| **NumPy** | Numerical operations and array handling. |
| **Scikit-learn (sklearn)** | Machine learning: `train_test_split`, `LabelEncoder`, `StandardScaler`, `LogisticRegression`, evaluation metrics. |
| **Matplotlib & Seaborn** | Generating a beautiful, publication-ready Confusion Matrix heatmap. |
| **Logging** | Recording each pipeline step and results to a file (`classification.log`) and console. |
| **OS / Sys** | Dynamic file path handling and graceful exit on critical errors. |
| **Git / GitHub** | Version control and submission. |

---

## 4. System Architecture

The architecture follows a strict, linear **"Pipeline"** pattern typical of ML engineering:

1. **Input/Data Load** – The script dynamically finds and loads `Dataset_for_Data_Analytics.xlsx`.
2. **Preprocessing** – Drops irrelevant columns (IDs, addresses), fills missing values.
3. **Encoding** – Converts all text (e.g., "Cash", "Laptop") to numeric codes.
4. **Split** – Divides data into Training (80%) and Testing (20%), maintaining class balance via stratification.
5. **Scaling** – Standardizes numeric features (UnitPrice, Quantity, etc.) to avoid scale bias.
6. **Model Training** – Fits a Logistic Regression model on the training set.
7. **Evaluation** – Tests the model on unseen data, prints metrics, saves files, plots confusion matrix.
8. **Interpretation** – Analyzes feature coefficients to explain model behavior.

### 4.1 Component Overview

| Component (Method) | Responsibility |
| :--- | :--- |
| `OrderStatusClassifier` | Main class encapsulating the entire ML pipeline. |
| `load_data()` | Reads Excel, handles file-not-found errors, logs initial target distribution. |
| `preprocess()` | Drops unique identifiers, fills missing `CouponCode`. |
| `encode_features()` | Applies `LabelEncoder` to all categorical columns and the target `y`. |
| `split_data()` | Splits data with `random_state=42` for reproducibility and `stratify` for class balance. |
| `scale_features()` | Uses `StandardScaler` to standardize numeric columns (fit on train, transform on test). |
| `train_model()` | Instantiates and trains `LogisticRegression(max_iter=1000)`. |
| `evaluate()` | Predicts on the test set, calculates accuracy, baseline, report, and triggers visualization. |
| `analyze_feature_importance()` | Interprets model coefficients to show top drivers for each class. |
| `run_pipeline()` | The master orchestrator that calls all methods in sequence. |

---

## 5. Project Structure

The repository is organized to keep code, data, generated outputs, and documentation separate:

```text
Task-2-HamzaAli/
├── classify_order_status.py          # Main application code (upgraded)
├── Dataset_for_Data_Analytics.xlsx   # Raw dataset (1200 orders)
├── README.md                         # Project documentation (this file)
├── classification.log                # Generated log file (auto-created on run)
├── classification_results.txt        # Saved metrics report
└── confusion_matrix.png              # Visual Confusion Matrix heatmap
