## Python Data Structures: Lists & Tuples

### 🛠️ Interactive Development Pro-Tip

* **Tab Completion:** Press **TAB** after a function name to view all available built-in methods.
* **The Underscore `_`:** In interactive sessions, the result of the last executed expression is automatically stored in the `_` variable.

---

### 📝 List: The Mutable Container `[]`

Lists are dynamic, growable structures designed for data that needs frequent updates.

#### **Key Properties**

* **Mutable:** You can add, remove, or change elements after creation.
* **Heterogeneous:** Can store mixed data types (e.g., `[1, "Data", 3.5]`).
* **Non-Strict:** Allows duplicate values and maintains order.

#### **Essential Methods**

* **Adding:** `append()` (add to end), `insert(index, value)` (add at specific spot), `extend()` (merge lists).
* **Removing:**
* `pop(index)`: Removes by **index** (defaults to the last item).
* `remove(value)`: Removes by the **first occurrence of the value**.
* `clear()`: Empties the list.


* **Utility:** `copy()` (clones the list), `reverse()` (flips order), `sort()` (arranges elements).

> **Sorting Rule:** Sorting only works if all elements are the **same data type**. Mixing strings and integers during a `sort()` will trigger an error.

---

### 🔒 Tuple: The Fixed Container `()`

Tuples are designed for data that should remain constant throughout the program.

* **Immutable:** Once created, elements cannot be changed, added, or removed.
* **Memory Efficient:** Faster than lists because their size is fixed.
* **Operations:** Supports indexing, slicing, and the `count()` method.

---

### ⚖️ List vs. Tuple: Quick Comparison

| Feature | List `[]` | Tuple `()` |
| --- | --- | --- |
| **Mutability** | Mutable (Editable) | Immutable (Constant) |
| **Size** | Growable | Fixed |
| **Methods** | Extensive (Append, Pop, etc.) | Limited (Count, Index) |
| **Performance** | Slower | Faster |
| **Use Case** | Dynamic datasets | Fixed configurations/coordinates |
