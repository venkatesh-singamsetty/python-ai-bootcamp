# OpenClaw Workshop

- **Workshop Repository**: [kodigitaccount/Moltbot_Clawdbot_Openclaw](https://github.com/kodigitaccount/Moltbot_Clawdbot_Openclaw)
- **Official Website**: [openclaw.ai](https://openclaw.ai/)
- **OpenClaw Tool Repository**: [openclaw/openclaw](https://github.com/openclaw/openclaw)

This guide covers setting up OpenClaw in **GitHub Codespaces**, configuring **OpenRouter** as the LLM provider, and integrating with a **Telegram Bot**.

## 1. Prerequisites & API Keys

Before starting the Codespace, obtain the necessary API keys.

### A. Get OpenRouter API Key
1.  Go to [OpenRouter.ai](https://openrouter.ai/).
2.  Sign up or log in.
3.  Navigate to **Keys** (or Account Settings).
4.  Click **Create Key**.
5.  Name it (e.g., `OpenClaw-Workshop`) and copy the key starting with `sk-or-...`.
    *   *Recommended Free Model*: `z-ai/glm-4.5-air:free` (or any other prefered model).

### B. Create Telegram Bot
1.  Open Telegram app.
2.  Search for **BotFather** (@BotFather) and verify it has the blue checkmark.
3.  Click **Start** or type `/start`.
4.  Send the command `/newbot`.
5.  Follow the prompts:
    *   **Name**: Choose a display name (e.g., `Venky OpenClaw Agent`).
    *   **Username**: Choose a unique username ending in `bot` (e.g., `venkatesh_openclaw_bot`).
6.  BotFather will reply with your **HTTP API Token**. Copy this token.

## 2. Setup GitHub Codespaces

1.  **Log in to GitHub**: Ensure you are signed in to your GitHub account.
2.  Navigate to the repository: [openclaw/openclaw](https://github.com/openclaw/openclaw).
3.  Click the green **Code** button.
4.  Switch to the **Codespaces** tab.
5.  Click **Create codespace on main**.
6.  Wait for the terminal environment to load completely.

> **Important Note on Uptime**: GitHub Codespaces are designed for development, not production hosting. They will **stop running** after a period of inactivity (usually 30 minutes). This means your Telegram bot will **not** stay online 24/7 here. For 24/7 hosting, you would need a VPS (like DigitalOcean, AWS EC2) or a platform like Railway/Heroku.

## 3. Install OpenClaw

In the Codespace terminal, run:

```bash
# Install OpenClaw globally
npm install -g openclaw@latest

# Verify installation
openclaw --version
```

## 4. Configure OpenClaw

For better security, we will configure API keys as environment variables and use the JSON configuration file for model and provider settings.

### A. Set Environment Variables
Export your API keys in the Codespace terminal. This prevents hardcoding secrets in files.

```bash
export OPENROUTER_API_KEY="sk-or-..."
export TELEGRAM_BOT_TOKEN="123456:ABC-..."
```

### B. Create Configuration File
Create the config directory and file:

```bash
mkdir -p ~/.openclaw
touch ~/.openclaw/openclaw.json
```

### C. Edit Configuration
Open `~/.openclaw/openclaw.json` and paste the following configuration. **Note:** we do not include the API keys here because they are already set in the environment.

```json
{
  "models": {
    "default": "z-ai/glm-4.5-air:free",
    "chat": "z-ai/glm-4.5-air:free"
  },
  "providers": {
    "openrouter": {
      "enabled": true
    }
  },
  "channels": {
    "telegram": {
      "enabled": true
    }
  }
}
```

## 5. Run & Integrate

### A. Start the Gateway
Start the OpenClaw gateway service:

```bash
openclaw gateway --verbose
```

> **Warning**: Even if this command is running, GitHub Codespaces **will still timeout** and shut down if you close the browser tab or stop interacting with the IDE for ~30 minutes. This is not suitable for a permanent bot.

### B. Pair with Telegram
1.  Open your bot in Telegram (e.g., `t.me/venkatesh_openclaw_bot`).
2.  Click **Start** or send `/start`.
3.  The bot should reply. If it asks for pairing, it will provide a code.
4.  If prompted with a code, run this command in your Codespace terminal (open a *new* terminal if the gateway is occupying the first one):
    ```bash
    openclaw pairing approve telegram <CODE_FROM_TELEGRAM>
    ```

### C. Chat!
You can now chat with your agent directly on Telegram. It will use the configured OpenRouter model (`glm-4.5-air` in this example) to respond.

## 6. Cleanup

Once you are done with the workshop, it is important to clean up to avoid racking up costs or leaving credentials exposed.

### A. Stop OpenClaw
If the gateway is running, press `Ctrl+C` in the terminal to stop it.

### B. Delete Codespace
1.  Go to [GitHub Codespaces](https://github.com/codespaces).
2.  Find the codespace you created for `openclaw/openclaw`.
3.  Click the **...** (three dots) menu and select **Delete**.

### C. Remove Integrations (Optional)
- **Telegram**: You can delete the bot in BotFather by sending `/deletebot`.
- **OpenRouter**: You can revoke the API keys in your OpenRouter account settings.
