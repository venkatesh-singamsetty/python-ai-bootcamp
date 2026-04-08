
# Agentic AI Stock App (Phidata + LangChain)

## Features
- Phidata Agent
- LangChain Agent
- Streamlit UI

---

## Run Locally

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

pip install -r requirements.txt
streamlit run app.py
```

---

## ☁️ Deploy to Amazon Linux EC2

### 1. Open AWS Firewall (Security Group)
Streamlit requires port `8501`. 
- Go to EC2 Console → Security Groups.
- Add an **Inbound Rule**: Type `Custom TCP`, Port `8501`, Source `0.0.0.0/0`.

### 2. Connect & Install System Dependencies
Connect to your EC2 instance via SSH:
```bash
ssh -i aws-venky-2026-key.pem ec2-user@3.137.205.41
```
Install Python 3.12, Git, and Tmux:
```bash
sudo dnf update -y
sudo dnf install python3.12 python3.12-pip git -y
#sudo dnf install tmux -y
```

### 3. Run the App Permanently in Background
To ensure the app doesn't die when you close your SSH terminal, use `tmux`:
```bash
# Start a new tmux session
# tmux new -s stockapp

# Copy code to EC2 instance
scp -i ~/Downloads/aws-venky-2026-key.pem requirements.txt app.py ec2-user@3.137.205.41:/home/ec2-user

# Navigate to your code folder & set up environment
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run the app
streamlit run app.py
```
*To detach from the terminal and leave it running, press `Ctrl + B`, let go, and then press `D`.*

You can now access your app at: `http://3.137.205.41:8501`
