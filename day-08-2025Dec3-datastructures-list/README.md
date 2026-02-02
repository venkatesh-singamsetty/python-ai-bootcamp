---

## Python Data Structures

**Built-in Data Structures:**  
- List, Tuple, Set, Dict, Range  

**User-Defined Data Structures:**  
- Array, Linked List, Tree  

**Notes:**  
- Scalar: single number  
- Vector: collection of scalars  
- Matrix: collection of vectors  
- Tensor: collection of matrices  

**Packages, Modules & Functions:**  
- Package/Framework/Library → Collection of modules  
- Module → Collection of functions  
- Function → Built-in or user-defined  

**List Operations:**  
- Define: `[]`  
- Append: `append()`  
- Copy: `copy()`  
- Clear: `clear()`  
- Delete: `del`

# Python Data Structures & Architecture

This section bridges the gap between basic variables and the complex data structures required for Data Science, along with the hierarchy of Python libraries.

---

## 🏗️ Data Structure Hierarchy
Understanding how data is organized is key to moving from a "fresher" mindset to a professional one.

| Concept | Capacity | Example |
| :--- | :--- | :--- |
| **Data Type** | Stores **only 1** value. | `a = 5` |
| **Data Structure** | Stores **multiple** values. | `a1 = [1, 2, 3]` |
| **Array (Matrix)** | Multi-dimensional numerical data. | 1D, 2D, or ND Arrays |
| **Dataframe** | Tabular data (**Rows × Columns**). | Excel sheets or SQL Tables |

### The Dimensional Ladder
* **Scalar:** A single number (e.g., `5`).
* **Vector:** A collection of scalars (1D).
* **Matrix:** A collection of vectors (2D).
* **Tensor:** A collection of matrices (ND) — *Crucial for Deep Learning.*

---

## 📚 Python Built-in vs. User-Defined Structures

### 1. Built-in Structures
* **List `[]`:** Heterogeneous (can store different data types like `[1, "NIT", 3.5]`).
* **Tuple `()`:** Immutable (cannot be changed).
* **Set `{}`:** Unique values only.
* **Dict `{k:v}`:** Key-Value pairs.
* **Range:** Generates a sequence of numbers.

### 2. User-Defined Structures
Handled by specific libraries (e.g., NumPy, Pandas, or collections):
* **Arrays:** Unlike lists, arrays are **Homogeneous** (all elements must be the same type).
* **Linked Lists / Trees:** Advanced structures used in specific algorithmic logic.

---

## 📦 Software Architecture: Packages vs. Modules
Think of Python's structure like a shopping mall to understand how to import tools:

> **Package (Library/Framework)** → A collection of Modules.
> **Module** → A collection of Functions.
> **Function** → The specific tool (In-built or User-defined).

**Real-world Example (The Shopping Mall):**
`from dmart_store.clothing import jeans`
* **Package:** `dmart_store`
* **Module:** `clothing`
* **Function:** `jeans`

**Machine Learning Example:**
`from sklearn.tree import DecisionTreeClassifier`
* **Package:** `sklearn` (Scikit-Learn)
* **Module:** `tree`
* **Function:** `DecisionTreeClassifier`



---

## 📝 Important Reminders for Technical Topics
* **List vs. Array:** A **List** is flexible (heterogeneous), while an **Array** is strict and optimized for math (homogeneous).
* **Data Management:** Companies work with Databases (DB), which are collections of Tables (**Dataframes**).
* **Class Strategy:** If your typing is slow, **listen and absorb the logic first**. Technical concepts are simple if you focus on the flow before the syntax.

---

## 📈 Final Accuracy Recap (Multi-Model Study)
As we move into tomorrow's session on **Lists `[]`**, remember our model performance benchmarks:
* **KNN:** 95% (Sensitive to data structure/outliers)
* **SVM:** 95% (Robust marginal distance)
* **Logit:** 92.5% (Stable baseline)
