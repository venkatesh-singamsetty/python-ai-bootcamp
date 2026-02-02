## Streamlit & Web Deployment: Study Notes

### 🌐 The Web Framework Landscape

In the industry, choosing a framework depends on the project's scale and the developer's expertise.

| Category | Frameworks | Best For... |
| --- | --- | --- |
| **Traditional Web** | Django, Flask, FastAPI | Scalable, custom, database-heavy websites. |
| **AI/Data Science** | **Streamlit**, Gradio | Rapidly turning Python scripts into interactive dashboards. |
| **Infrastructure** | Docker, Kubernetes | Packaging and scaling apps in the cloud. |

---

### 🎨 Streamlit: Python-Powered UI

Streamlit allows you to build a frontend without writing HTML or CSS.

#### **Core UI Components**

* **`st.write()`**: The most versatile command; it automatically detects and renders text, tables, or charts.
* **`st.title()` / `st.header()**`: Defines the visual hierarchy of your page.
* **`st.sidebar`**: Used to move inputs (like sliders or dropdowns) to a left-side panel, keeping the main area for results.

#### **Interactive Widgets**

* **`st.dataframe()`**: Displays interactive tables (perfect for our IPL dataset).
* **`st.selectbox()`**: Creates a dropdown menu (e.g., Select a Team).
* **`st.button()`**: Triggers specific logic (e.g., Run Prediction).

---

### 🛠️ Local Execution & Verification

Streamlit apps are not run like standard Python scripts (`python app.py`). They require the Streamlit server to be initialized via the terminal.

**Command Syntax:**

```bash
# General command
streamlit run filename.py

# Examples from our project
streamlit run app.py
streamlit run intro.py

```

**Accessing the App:**
Once the command is executed, verify the deployment by visiting the local host address in your web browser:

> **http://localhost:8501**

---

### 🚀 The Deployment Pipeline

To deliver a project to a client like **ESPN** or **Star Sports**, follow this industry-standard workflow:

1. **Logic:** Write the Python backend (Pandas analysis, ML models).
2. **UI:** Wrap the logic in **Streamlit** components for user interaction.
3. **Package:** Create a **Docker** container to ensure all dependencies (NumPy, PIL, Pandas) work on any server.
4. **Launch:** Deploy to a cloud provider so the client can access it via a URL.

---

### 💡 Key Shift in Mindset

* **Terminal Era:** We used `print()` for output and `input()` for data.
* **Web Era:** We use `st.write()` for output and `st.text_input()` (or other widgets) for user data.
