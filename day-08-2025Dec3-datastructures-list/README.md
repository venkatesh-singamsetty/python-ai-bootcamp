## Python Data Structures & Architecture: Study Notes

### 🏗️ Data Organization Hierarchy

Modern data science moves from simple values to multi-dimensional structures.

| Concept | Capacity | Example |
| --- | --- | --- |
| **Data Type** | Stores **1** value (Scalar). | `x = 10` |
| **Data Structure** | Stores **multiple** values. | `list = [1, 2, 3]` |
| **Array (Matrix)** | Multi-dimensional numerical data. | 1D, 2D, or ND Arrays |
| **Dataframe** | Tabular data (**Rows × Columns**). | Excel or SQL Tables |

#### **The Dimensional Ladder (Tensors)**

1. **Scalar:** A single number (0D).
2. **Vector:** A sequence of scalars (1D).
3. **Matrix:** A grid of vectors (2D).
4. **Tensor:** A stack of matrices (ND) — *The backbone of Deep Learning.*

---

### 📚 Python Data Structure Categories

#### **1. Built-in Structures**

* **List `[]`:** **Heterogeneous** (can mix types like `[1, "Data", 3.14]`).
* **Tuple `()`:** **Immutable** (cannot be edited after creation).
* **Set `{}`:** Unordered collection of **unique** values only.
* **Dict `{k:v}`:** Maps **Key-Value** pairs for fast lookups.
* **Range:** Efficiently generates a sequence of integers.

#### **2. User-Defined & Specialized Structures**

* **Arrays:** **Homogeneous** (all elements must be the same type). Optimized for mathematical operations via NumPy.
* **Linked Lists / Trees:** Advanced logic structures for specific algorithmic needs.

---

### 📦 Python Software Architecture

To import tools correctly, visualize the hierarchy from broad to specific:

* **Package (Library/Framework):** A directory containing multiple modules (e.g., `sklearn`).
* **Module:** A single `.py` file containing related functions (e.g., `tree`).
* **Function:** A specific block of code designed to perform a task (e.g., `DecisionTreeClassifier`).

**Syntax Example:** `from package.module import function`

---

### 🛠️ Common List Operations

* **Define:** Created using square brackets `[]`.
* **`append()`:** Adds an element to the end.
* **`copy()`:** Returns a shallow copy of the list.
* **`clear()`:** Removes all elements from the list.
* **`del`:** A keyword to delete an element by index or remove the entire list.

---

### 💡 Key Technical Distinctions

* **Lists vs. Arrays:** Lists are flexible and can hold different types; Arrays are strict (homogeneous) but significantly faster for math.
* **Business Logic:** Databases (DB) are essentially collections of Tables, which Python handles as **Dataframes**.
