# Machine Learning & AI Learning Notes

This repository contains structured notes and learning roadmap for **Machine Learning (ML)**, **AI**, **Gen AI**, and **MLOps** concepts, including practical ML workflows, models, and frameworks.

---

## Table of Contents

1. [Data Processing Pipeline](#data-processing-pipeline)  
2. [ML Model Parameters vs LLM Parameters](#ml-model-parameters-vs-llm-parameters)  
3. [Feature Engineering](#feature-engineering)  
4. [ML Models](#ml-models)  
   - [Regression](#regression-models)  
   - [Classification](#classification-models)  
   - [Clustering](#clustering-models)  
5. [MLOps / CI-CD](#mlops)  
6. [AI & Generative AI](#ai-and-generative-ai)  
7. [Frameworks & Libraries](#frameworks-and-libraries)  
8. [Integration & Real-World Usage](#integration-and-real-world-usage)

---

## Data Processing Pipeline

A typical **ML data processing workflow**:

1. **Dataset import** – Load the data.  
2. **Define variables** – Separate independent (`X`) and dependent (`y`) variables.  
3. **Data cleaning** – Handle missing values and perform EDA (Exploratory Data Analysis).  
4. **Train-test split** – Split `X` into `X_train` and `X_test`; `y` into `y_train` and `y_test`.  
5. **Feature Engineering** – Apply feature selection, scaling, and transformations.

### Missing Values Handling

- Use **`SimpleImputer`** from `sklearn.impute` to fill missing values.  
- `fit` and `transform` methods are used to learn and apply imputations.  
- Default strategy: **mean**  
- Hyperparameter tuning: User can change strategy to **median**, **most frequent**, etc.

> **Tip:** Shuffling values may impact model accuracy; always evaluate after shuffling.

---

## ML Model Parameters vs LLM Parameters

- **ML Model Parameters**: Learned during training (e.g., coefficients in regression).  
- **Hyperparameters**: Set by user, control training (e.g., imputer strategy, number of trees in Random Forest).  
- **LLM Parameters**: Millions/billions of learned weights controlling language model behavior.  

> Use hyperparameter tuning to improve ML model accuracy if default parameters don’t meet requirements.

---

## Feature Engineering

1. **EDA Techniques** – Identify patterns, distributions, and anomalies.  
2. **Feature Selection** – e.g., Recursive Feature Elimination (RFE).  
3. **Feature Scaling** – Normalization, Standardization.  

---

## ML Models

### Regression Models

- Simple Linear Regression  
- Multiple Linear Regression  
- Polynomial Regression  
- Regularization (L1 / Lasso, L2 / Ridge)  
- Time Series Regression (pre-RNN concepts)  
- ANN Regression  

> Example project: Apply 14 regression algorithms at once for comparison.

### Classification Models

- Logistic Regression  
- Support Vector Machine (SVM)  
- K-Nearest Neighbors (KNN)  
- Decision Tree  
- Random Forest  
- Naive Bayes  
- XGBoost  
- LightGBM (LGBM)  
- ANN Classifier  

### Clustering Models

- PCA (Principal Component Analysis)  
- K-Means Clustering  
- Hierarchical Clustering  

---

## MLOps / CI-CD

- Implement CI/CD pipelines for ML workflows  
- Automate model training, testing, and deployment  

---

## AI and Generative AI

### AI Concepts

- **Supervised Learning (ML)** – Interacts with structured data (tabular datasets).  
- **Unsupervised Learning (AI)** – Interacts with text, images, video, streaming data, APIs.  
- **Generative AI / Agentic AI** – Reinforcement learning; interacts with environment.  

### Areas of Focus

- NLP (Natural Language Processing)  
- Deep Learning (DL)  
- Neural Networks (NN)  
- Computer Vision (CV)  
- LLM (Large Language Models)  
- Prompt Engineering  

---

## Frameworks and Libraries

- **Scikit-learn (`sklearn`)**  
  - `sklearn.impute` – Handle missing data  
  - `sklearn.model_selection` – Train-test split, cross-validation  
  - `sklearn.preprocessing` – Scaling, normalization  
- **XGBoost** – Gradient boosting library  
- **LightGBM** – Gradient boosting framework for high performance  

---

## Integration and Real-World Usage

- Apply these ML/AI learnings to **day-to-day projects**  
- Understand **ecosystem management**: Clients, teams, and data pipelines  
- Avoid connecting Java directly to AI pipelines; focus on **data architecture**  
- Aim to automate ML models to reduce manual intervention and scale solutions  
