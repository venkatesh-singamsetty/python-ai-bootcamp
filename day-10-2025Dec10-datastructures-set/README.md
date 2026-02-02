## Python Sets: Complete Reference

### 🧱 Core Properties

A **set** is a collection used for storing unique elements where order doesn't matter.

* **Unordered & Unindexed:** You cannot access elements via `s[0]`.
* **Unique Only:** Automatically filters out duplicate values.
* **Mutable Container:** You can add or remove items from the set itself.
* **Immutable Elements:** While the set is mutable, the **items inside** must be immutable (e.g., integers, strings, or tuples). You cannot put a list inside a set.

---

### ➕ Modification Methods

| Method | Behavior | Error Handling |
| --- | --- | --- |
| **`add()`** | Adds a single element to the set. | Ignores if already present. |
| **`discard()`** | Removes a specific element. | **Safe:** Does nothing if element is missing. |
| **`remove()`** | Removes a specific element. | **Strict:** Raises `KeyError` if missing. |
| **`pop()`** | Removes and returns a random element. | Raises `KeyError` if set is empty. |

---

### 🔀 Mathematical Set Operations

Sets excel at finding relationships between two groups of data.

* **Union (`|`):** Combines all elements from both sets.
* **Intersection (`&`):** Keeps only elements found in **both** sets.
* **Difference (`-`):** Elements in the first set that are **not** in the second.
* **Symmetric Difference (`^`):** Elements in either set, but **not both** (excludes the intersection).

---

### 👨‍👦 Relationship Methods

Use these to check how one set relates to another:

| Method | Meaning | Memory Trick |
| --- | --- | --- |
| **`issuperset()`** | Does Set A contain everything in Set B? | **Dad** (The larger entity) |
| **`issubset()`** | Is Set A entirely contained within Set B? | **Son** (The smaller entity) |
| **`isdisjoint()`** | Do the sets have **zero** common values? | **Neighbor** (Separate houses) |

---

### 💡 Quick Comparison: discard() vs remove()

Choosing the right deletion method depends on how you want to handle missing data:

* Use **`discard()`** when it’s okay if the item isn't there (prevents code crashes).
* Use **`remove()`** when the item **must** be present for your logic to be valid.
