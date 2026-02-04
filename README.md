## **Course Name:** Python with Generative AI & Agentic AI Bootcamp
- AI: NLP, DL, Neural Networks  
- Gen AI: AI tools for generating content  
- Agentic AI: AI tools for automating projects  

---

## Class Recorings
https://learn.nareshit.com/users/sign_in

---

## **Google Classroom Notes Download:**  
1. Install WinRAR/WinZip  
2. Open notes → 3 dots → Open in new tab → Download  
3. Extract files  
4. Open `.pdf` with PDF reader; `.py` or `.ipynb` with VS Code/Jupyter  

---

## Mentorship & Support

**Online Mentor Links:**  
- [Data Science Mentor 1](https://zoom.us/j/82068816627?pwd=3BYepgjDCqbkroxauQGo2T4gr9f7Fn.1)  
- [Data Science Mentor 2](https://zoom.us/j/86433658207?pwd=7abh6fYZ1McPZsguCNgEaONRoKKY7Y.1)  
**Password:** 112233  

**Offline Mentor:** 3rd Floor  

---

## Demo Recording Sessions

| Day | Link |
|-----|------|
| 1   | [YouTube](https://youtu.be/FstXAG5czbo) |
| 2   | [YouTube](https://youtube.com/live/oKzJ5BE8vVc?feature=share) |
| 3   | [YouTube](https://youtu.be/Hgx5S1JNbTA) |
| 4   | [YouTube](https://youtu.be/U5KBo4GWxEY) |
| 5   | [YouTube](https://youtu.be/hAS0Mmh_SdU) |
| 6   | [YouTube](https://youtu.be/yW5wxTqLiVE) |
| 7   | [YouTube](https://youtu.be/U5-QMGhtSpE) |
| 8   | [YouTube](https://youtu.be/RdMPrFRNg_s) |
| 9   | [YouTube](https://youtu.be/QN2U2LuNHxw) |
| 10  | [YouTube](https://youtu.be/MTSA5ugdQTE) |
| 11  | [YouTube](https://youtu.be/RfneQ_xaPHA) |
| 12  | [YouTube](https://youtu.be/DwdyBLgyYuU) |

**Drive Link:** [Google Drive](https://drive.google.com/drive/u/0/folders/18jHbEiaw6SSBZEuKmioWqM1bjV0no0Y7)  
**WhatsApp Group:** [Link](https://chat.whatsapp.com/JmT4KftAduU7kP7dNEoTV0)  

---

## Admin Details

- Online Admin: +91 9154861173 (Mr. Areef)  
- Online Admin: +91 9133343369 (Leena Madam)  
- Offline Admin: Mr. Bheem  

#### Prakash Senapathi Sir: +91 935-315-7658

## Python Software Installation Video: [YouTube](https://youtu.be/PhIAQ8rE2xc?si=_AhLmMSbwR8170Mz)

## Push changes to remote repository
```bash
DATE='day-48-2026Feb4-ml-ensamble-learning'
cd /Users/venkat/workspace/gitRepos/python-genAi-agenticAI
mkdir -p ${DATE}

mv ~/Downloads/Advanced\ \ Bootcamp\ \ on\ Gen\ AI\ \&\ Agentict\ AI.rar .
mv ~/Downloads/Regular\ Summarization_\ 530\ PM.rar .
tar -xf Advanced\ \ Bootcamp\ \ on\ Gen\ AI\ \&\ Agentict\ AI.rar
tar -xf Regular\ Summarization_\ 530\ PM.rar
rm *.rar

cd ${DATE}
mv /Users/venkat/Downloads/tmp.rar .
tar -xf tmp.rar
rm tmp.rar
cd ..

DATE='day-49-2026Feb4-ml-xgboost'
cd /Users/venkat/workspace/gitRepos/python-genAi-agenticAI
mkdir -p ${DATE}
touch ${DATE}/README.md
touch ${DATE}/app.py

git add .
git commit -m "Updated ${DATE}"; git push origin develop; git status
```

```bash
python3.12 -m venv .venv

source .venv/bin/activate
python3.12 -m pip install --upgrade pip

python3.12 -m pip install streamlit scikit-learn

python3.12 -m streamlit run app.py
```
 