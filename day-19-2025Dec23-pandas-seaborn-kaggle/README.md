## Visualization & Global Data Resources: Study Notes

### 🎨 Matplotlib & Seaborn

These libraries transform raw numbers into visual stories during **Exploratory Data Analysis (EDA)**.

* **Matplotlib:** The foundational "engine" for plotting in Python. It offers maximum control but requires more code for styling.
* **Seaborn:** Built on top of Matplotlib. It simplifies complex statistical visualizations and provides aesthetically pleasing default themes.

---

### 📊 Levels of Analysis

Visualization is categorized by the number of variables (features) being studied simultaneously.

#### **1. Univariate Analysis (1 Variable)**

* **Goal:** Understand the distribution, frequency, and spread of a single feature.
* **Common Plots:** Histogram, Count Plot, and Box Plot.

#### **2. Bivariate Analysis (2 Variables)**

* **Goal:** Determine the relationship or correlation between two features.
* **Common Plots:** Scatter Plot (correlation), Line Plot (trends), and Bar Plot (comparison).

#### **3. Multivariate Analysis (3+ Variables)**

* **Goal:** Uncover complex interactions within the data.
* **Common Plots:** * **Heatmap:** Visualizes correlation matrices using colors.
* **Pair Plot:** Generates a grid of scatter plots for all variable combinations.
* **Facet Plots:** Displays multiple charts based on a categorical variable.



---

### 🔍 Outlier & Anomaly Detection

An **outlier** is a data point that deviates significantly from the rest of the dataset.

* **Detection Tool:** The **Box Plot** is the primary visual method for identifying outliers (points appearing outside the "whiskers").
* **Impact:** Outliers can skew your mean and decrease model accuracy; detecting them is vital for data cleaning.

---

### 🌐 The Data Scientist's Toolkit (Resources)

Professional analysts rely on global repositories for datasets and pre-trained models.

* **Kaggle:** The premier platform for data science competitions, datasets, and community notebooks.
* **Hugging Face:** The "GitHub for AI"—the primary source for downloading **Generative AI** and **LLM** models.
* **UCI Machine Learning Repository:** A classic source for academic and standard ML datasets.
* **MovieLens Dataset:** A standard benchmark dataset for building recommendation systems (includes `movie.csv`, `rating.csv`, and `tag.csv`).

---

### ⚙️ Practical Data Handling

* **Python vs. Excel:** While Excel is limited to ~10 lakh () rows, Python (Pandas) can effortlessly process massive datasets (e.g.,  records).
* **File Management:** Use magic commands like `%cd` (change directory) and `%ls` (list files) to navigate your local workspace within Jupyter/Colab.
