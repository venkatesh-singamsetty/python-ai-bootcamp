- [Streamlit](https://streamlit.io/)
- [Streamlit Documentation](https://docs.streamlit.io/)

```bash
% streamlit run app.py

% streamlit run intro.py

% streamlit run code1.py
```
- Verify http://localhost:8501

# 🌐 Web Deployment & AI Frameworks

This section covers how to turn your Python logic and AI models into professional web applications using industry-standard frameworks and cloud tools.

---

## 🏗️ The Framework Landscape

Choosing the right tool depends on whether you are building a full-scale web service or a quick AI prototype.

### 1. Traditional Web Frameworks
Used for building robust, scalable websites that require custom HTML/CSS and complex backend logic.
* **Django:** "Batteries included"—best for large, database-heavy applications.
* **Flask:** Minimalist and flexible; great for microservices.
* **FastAPI:** Modern and high-performance; optimized for building APIs.

### 2. AI & LLM Frameworks
Designed specifically for Data Scientists to build apps **entirely in Python** without needing to write HTML.
* **Streamlit:** The gold standard for interactive dashboards and data apps.
* **Gradio:** Excellent for creating quick demos, especially for LLMs and image models.

### 3. Cloud & Infrastructure
To make your app accessible to the world (like our ESPN/Star Sports clients), we use:
* **Docker:** To package the app so it runs the same on any machine.
* **Kubernetes:** To manage and scale multiple Docker containers in the cloud.

---

## 🎨 Streamlit: Your Frontend Toolkit
Streamlit allows you to "paint" your UI using simple Python commands.



### Text & Layout Elements
* `st.title()`: The main heading of your app.
* `st.header()` / `st.subheader()`: Organized section titles.
* `st.write()`: The "Swiss Army Knife"—renders text, dataframes, and charts.

### The Sidebar (Navigation & Filters)
The sidebar keeps your main content clean by moving controls to the left.
* `st.sidebar.header()`: A title inside the sidebar.
* `st.sidebar.text_input()`: For entering text (like an API Key).
* `st.sidebar.slider()`: For selecting numerical ranges (like a model's Temperature).
* `st.sidebar.selectbox()`: A dropdown menu (ideal for picking an IPL Team).

### Interactive Widgets
* `st.dataframe()`: Displays an interactive table of your data.
* `st.checkbox()`: Boolean toggle (e.g., "Show Raw Data").
* `st.button()`: Triggers an action (e.g., "Predict Winner").

---

## 🚀 Pro-Deployment Workflow
1. **Develop:** Build your logic in Python using the tools we've learned.
2. **Interface:** Use **Streamlit** to create the UI buttons and sliders.
3. **Containerize:** Use **Docker** to ensure all libraries (Pillow, NumPy, Pandas) are packaged.
4. **Deploy:** Push to the cloud so clients can interact with your **Agentic AI** project.

> **Note:** Remember that `input()` works in the terminal, but `st.text_input()` is what you need for a web-based user interface.

---

## 📈 Summary of Progress
* [x] **Backend Logic:** Loops, Conditionals, Functions.
* [x] **Data Processing:** NumPy, Pandas, Handling Nulls.
* [x] **Visualization:** Seaborn Outliers and Bivariate Analysis.
* [x] **Deployment:** Streamlit UI components and Cloud infrastructure.
