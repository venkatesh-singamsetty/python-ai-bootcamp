## MATLIBPLOT -> R G B
- https://matplotlib.org/stable/users/explain/colors/colormaps.html

## PIL & Random Seeds: Study Notes

### 🖼️ PIL (Python Imaging Library)

The **PIL** library (now commonly maintained as **Pillow**) is the standard tool for opening, manipulating, and saving many different image file formats in Python.

* **Core Functionality:** Used for resizing, cropping, rotating, and changing image colors (e.g., converting RGB to Grayscale).
* **Integration:** Often used alongside **NumPy** to convert images into arrays of pixels, which is essential for training Computer Vision models (CNNs).
* **Common Usage:**
```python
from PIL import Image
img = Image.open('dataset_image.jpg')
```

---

### 🎲 `np.random.seed()`

In Machine Learning, we often need "random" numbers for initializing weights or shuffling data. However, for results to be scientific, they must be **reproducible**.

* **The Problem:** Without a seed, `np.random.rand()` produces different numbers every time you run the code.
* **The Fix:** `np.random.seed(value)` fixes the sequence of "random" numbers.
* **Mechanism:** It locks the internal algorithm to a specific starting point. If two people use the same seed, they will get the exact same "random" results.

#### **Example Comparison:**

| Without Seed | With `np.random.seed(42)` |
| --- | --- |
| Run 1: `0.123, 0.456, 0.789` | Run 1: `0.374, 0.950, 0.731` |
| Run 2: `0.987, 0.654, 0.321` | Run 2: **`0.374, 0.950, 0.731`** |

---

### 💡 Why this matters in AI/ML

* **PIL:** Is the "eyes" of your model—it prepares the visual data.
* **Seed:** Ensures that when you tell a teammate your model is **95% accurate**, they can run the same code and get the exact same **95%** result.
