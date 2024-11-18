
#!/bin/bash

echo "Starting Workspace Setup..."

# Pull latest changes from GitHub (if applicable)
if [ -d ".git" ]; then
    echo "Pulling latest changes from GitHub..."
    git pull origin main
else
    echo "No Git repository found. Skipping pull step."
fi

# Set up Python environment
echo "Installing required Python packages..."
pip install -r requirements.txt

# Set up environment variables
if [ ! -f config/.env ]; then
    echo "No .env file found in config/. Creating a default one."
    echo "OPENAI_API_KEY=<your-key>" > config/.env
    echo "GITHUB_TOKEN=<your-token>" >> config/.env
fi

# Start the Beta Mode Dashboard
echo "Starting Beta Mode Dashboard..."
python scripts/beta_dashboard.py
