## EDA: The Foundation of Machine Learning

Exploratory Data Analysis (EDA) is the mandatory process of cleaning and understanding raw data. In the industry, **80% of a Data Scientist's time** is spent on EDA because "Bad Data = Bad Model."

---

## 🏗️ The 7-Step EDA Workflow

### 0. Business Understanding

Before touching code, understand the domain (Banking, Supply Chain, FMCG). ML must solve a business problem, usually centered around the customer.

### 1. Variable Identification

* **Independent Variables (IV / ):** The input features (the "Causes").
* **Dependent Variable (DV / ):** The target variable (the "Effect" you want to predict).
  - **ML Logic:** y = f(x) or y = m_1x_1 + m_2x_2 + ...

### 2. Univariate Analysis

Analysis of **one** variable to check its distribution, Mean/Median/Mode, and Skewness.

### 3. Bivariate Analysis

Analyzing the relationship between **two** variables (e.g., how Experience affects Salary).

### 4 & 5. Outlier & Missing Value Treatment

Extreme values (Outliers) and gaps (Missing Values) must be handled via removal or capping to prevent model bias.

### 6. Variable Imputation

Filling missing data using statistical methods:

* **Mean/Median:** For numerical data.
* **Mode:** For categorical data.
* **Fill:** Forward or backward filling.

### 7. Feature Engineering (Variable Creation)

Transforming raw data into meaningful features (e.g., extracting "Year" from a date string).

---

## 🤖 Machine Learning Map

Machine Learning is categorized based on the data type and the goal.

### 1. Supervised Learning (Labeled Data)

Stored in SQL databases. The model knows the "answer" during training.

* **Regression (Continuous Y):** Predicting prices (House, Stock, Gold).
* **Classification (Categorical Y):** Predicting labels (Spam/Not Spam, Fraud/Safe).

### 2. Unsupervised Learning (Unlabeled Data)

Stored in NoSQL databases. The model finds hidden patterns on its own.

* **Clustering:** Grouping similar items together (e.g., Customer Segmentation).
* **Dimensionality Reduction:** Simplifying data (PCA).

### 3. Reinforcement Learning

Learning through trial and error using an **Agent** and an **Environment** based on rewards and punishments.

---

## 🚀 Key Takeaway

You cannot build a house without a foundation, and you cannot build a model without EDA. A simple algorithm on clean data will always outperform a complex algorithm on dirty data.
