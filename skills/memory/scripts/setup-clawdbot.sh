#!/bin/bash
# setup-clawdbot.sh - Interactive Clawdbot setup helper
# Run this after the instance is provisioned

set -e

echo "=== Clawdbot AI Employee Setup ==="
echo ""

# Ensure NVM is loaded
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Check prerequisites
echo "Checking prerequisites..."

if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js not found. Please install Node.js 22+"
    exit 1
fi

NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 22 ]; then
    echo "ERROR: Node.js 22+ required (found v$NODE_VERSION)"
    exit 1
fi
echo "  Node.js: $(node -v) ✓"

if ! command -v clawdbot &> /dev/null; then
    echo "Installing Clawdbot..."
    npm install -g clawdbot@latest
fi
echo "  Clawdbot: $(clawdbot --version 2>/dev/null || echo 'installed') ✓"

if ! command -v gh &> /dev/null; then
    echo "WARNING: GitHub CLI not found. Install with: sudo apt install gh"
else
    echo "  GitHub CLI: $(gh --version | head -1) ✓"
fi

echo ""
echo "Prerequisites check complete!"
echo ""

# Menu
while true; do
    echo "=== Setup Menu ==="
    echo "1) Run Clawdbot onboarding wizard"
    echo "2) Configure Anthropic API key"
    echo "3) Connect WhatsApp"
    echo "4) Connect Telegram"
    echo "5) Connect Discord"
    echo "6) Connect Slack"
    echo "7) Check Clawdbot status"
    echo "8) Apply full autonomy config"
    echo "9) Authenticate GitHub CLI"
    echo "0) Exit"
    echo ""
    read -p "Select option: " choice

    case $choice in
        1)
            echo ""
            echo "Running Clawdbot onboarding..."
            clawdbot onboard --install-daemon
            echo ""
            ;;
        2)
            echo ""
            read -p "Enter your Anthropic API key: " api_key
            clawdbot config set anthropic.apiKey "$api_key"
            echo "API key configured!"
            echo ""
            ;;
        3)
            echo ""
            echo "Starting WhatsApp login..."
            echo "A QR code will appear - scan it with WhatsApp on your phone"
            clawdbot channels login whatsapp
            echo ""
            ;;
        4)
            echo ""
            echo "To set up Telegram:"
            echo "1. Message @BotFather on Telegram"
            echo "2. Send /newbot and follow instructions"
            echo "3. Copy the bot token"
            read -p "Enter your Telegram bot token: " telegram_token
            clawdbot channels add telegram --token "$telegram_token"
            echo "Telegram bot configured!"
            echo ""
            ;;
        5)
            echo ""
            echo "To set up Discord:"
            echo "1. Go to https://discord.com/developers/applications"
            echo "2. Create a new application"
            echo "3. Go to Bot section, create bot, copy token"
            echo "4. Enable MESSAGE CONTENT INTENT in Bot settings"
            echo "5. Use OAuth2 URL Generator to invite bot to your server"
            read -p "Enter your Discord bot token: " discord_token
            clawdbot channels add discord --token "$discord_token"
            echo "Discord bot configured!"
            echo ""
            ;;
        6)
            echo ""
            echo "To set up Slack:"
            echo "1. Go to https://api.slack.com/apps"
            echo "2. Create a new app (from manifest or scratch)"
            echo "3. Add bot scopes: chat:write, app_mentions:read, im:history, etc."
            echo "4. Install to workspace"
            echo "5. Copy Bot User OAuth Token and App-Level Token"
            read -p "Enter Slack Bot Token (xoxb-...): " slack_bot_token
            read -p "Enter Slack App Token (xapp-...): " slack_app_token
            clawdbot channels add slack --bot-token "$slack_bot_token" --app-token "$slack_app_token"
            echo "Slack bot configured!"
            echo ""
            ;;
        7)
            echo ""
            clawdbot status
            echo ""
            ;;
        8)
            echo ""
            echo "Applying full autonomy configuration..."
            cp ~/clawd/config/clawdbot.example.json ~/.clawdbot/config.json 2>/dev/null || \
                echo "Note: Copy the example config manually if needed"
            echo "Clearing exec approvals for full autonomy..."
            echo "[]" > ~/.clawdbot/exec-approvals.json 2>/dev/null || true
            echo "Full autonomy config applied!"
            echo ""
            ;;
        9)
            echo ""
            echo "Authenticating GitHub CLI..."
            gh auth login
            echo ""
            ;;
        0)
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid option"
            echo ""
            ;;
    esac
done
