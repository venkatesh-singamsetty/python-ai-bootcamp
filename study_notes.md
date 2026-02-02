# 📚 Python GenAI & Agentic AI Bootcamp - Study Notes

## Phase 1: Foundations & Setup 🛠️

### 1. Developer Environment
- **IDE:** VS Code (Recommended) with extensions (Python, Jupyter, GitHub Copilot).
- **Alternative Environments:** Anaconda (Jupyter/Spyder), Google Colab (Cloud GPU access).
- **Version Control:** GitHub (Public vs Private Repositories).

### 2. Python Basics
- **Variables:** Identifiers for values. Case-sensitive, no leading digits, `_` allowed.
- **Data Types:** `int` (whole), `float` (decimal), `bool` (logic), `str` (text), `complex`.
- **Operators:**
  - **Arithmetic:** `+`, `-`, `*`, `/`, `//` (floor), `%` (modulus), `**` (power).
  - **Logical:** `and`, `or`, `not`.
  - **Bitwise:** `&`, `|`, `^`, `~`, `<<`, `>>`.
- **Number Systems:** Binary (`0b`), Octal (`0o`), Hexadecimal (`0x`).

### 3. Data Structures
| Structure | Syntax | Mutability | Ordered | Descriptions |
| :--- | :--- | :--- | :--- | :--- |
| **List** | `[]` | Mutable | Yes | Dynamic, heterogeneous collections. |
| **Tuple** | `()` | Immutable | Yes | Fixed, faster, memory-efficient. |
| **Set** | `{}` | Mutable | No | Unique elements only, mathematical ops. |
| **Dict** | `{k:v}`| Mutable | Yes | Key-Value pairs, fast lookups. |

### 4. Control Flow & Functions
- **Loops:** `for` (sequences), `while` (conditions).
- **Conditionals:** `if`, `elif`, `else`.
- **Functions:** Reusable blocks `def name(params):`.
  - **Polymorphism:** Same function behavior on different types (e.g., `len()`).

---

## Phase 2: Data Science & Engineering 📊

### 1. Data Manipulation (Pandas)
- **DataFrame:** Tabular data structure (rows & columns).
- **Inspection:** `head()`, `tail()`, `info()`, `describe()`.
- **Cleaning:** Handling missing values, duplicates, and type conversions.

### 2. Visualization
- **Matplotlib:** Fundamental plotting library.
- **Seaborn:** High-level statistical visualization.
- **Analysis Levels:**
  - **Univariate:** One variable (Histograms, Boxplots).
  - **Bivariate:** Two variables (Scatter plots, Correlations).
  - **Multivariate:** 3+ variables (Heatmaps, Pairplots).

### 3. Exploratory Data Analysis (EDA) - 7 Steps
1.  **Variable Identification:** Input vs Target.
2.  **Univariate Analysis:** Understand distribution.
3.  **Bivariate Analysis:** Understand relationships.
4.  **Outlier Treatment:** Boxplots, Z-Score.
5.  **Missing Value Treatment:** Imputation (Mean/Median/Mode).
6.  **Variable Transformation:** Encoding (Label/One-Hot), Scaling.
7.  **Feature Engineering:** Creating new meaningful variables.

---

## Phase 3: Statistics 📉

### 1. Core Concepts
- **Population vs Sample:** Total set vs Subset used for analysis.
- **Normal Distribution:** Symmetrical bell curve (Mean = Median = Mode).
- **Skewness:** Left (Negative) vs Right (Positive) skew.

### 2. Inferential Statistics
- **Hypothesis Testing:** Making decisions about populations based on samples.
- **Confidence Intervals (CI):** Range of values likely to contain the population parameter.
- **Standard Error:** Measure of statistical accuracy.

---

## Phase 4: Machine Learning 🤖

### 1. Learning Paradigms
- **Supervised:** Labeled data (Regression, Classification).
- **Unsupervised:** Unlabeled data (Clustering, Dimensionality Reduction).
- **Reinforcement:** Agent learns via rewards/penalties.

### 2. Algorithms
- **Regression (Predicting Outcomes):**
  - Simple Linear Regression (SLR): `y = mx + c`
  - Multiple Linear Regression (MLR): `y = b0 + b1x1 + ... + bnxn`
  - Polynomial Regression: Modeling curvature.
- **Classification (Predicting Categories):**
  - Logistic Regression: Binary outcomes (Sigmoid function).
  - KNN (K-Nearest Neighbors): Distance-based classification.
  - Naive Bayes: Probabilistic (great for text/NLP).
  - SVM (Support Vector Machines): Hyperplane separation.
  - Decision Trees: Rule-based splitting.

### 3. Evaluation Metrics
- **Regression:** MAE, MSE, RMSE, R2 Score.
- **Classification:** Accuracy, Precision, Recall, F1-Score, Confusion Matrix.
- **Bias-Variance Tradeoff:**
  - **Underfitting (High Bias):** Model makes strong assumptions, misses patterns.
  - **Overfitting (High Variance):** Model memorizes noise, fails to generalize.

### 4. Optimization
- **Feature Scaling:** StandardScaler (Z-score), MinMaxScaler.
- **Regularization:** L1 (Lasso), L2 (Ridge) to reduce overfitting.
- **Handling Imbalance:** SMOTE (Synthetic Minority Over-sampling Technique).

---

## Phase 5: Generative AI & Deployment 🚀

### 1. GenAI Concepts
- **GenAI vs Agentic AI:**
  - **GenAI:** Creates content (Text, Image, Code).
  - **Agentic AI:** Plans, Reasons, Acts (Tools, API calls).
- **LLMs:** Large Language Models (Ollama, OpenAI, Gemini).

### 2. MLOps & Web
- **Model Persistence:** `pickle` for serializing (saving) models.
- **Web Frameworks:**
  - **Streamlit:** Rapid data apps.
  - **Gradio:** Simple UI for ML models.
