
#!/bin/bash

# Clone repository and set up the environment
echo "Cloning repository..."
git clone <YOUR_REPO_URL> project
cd project

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Start the development server
echo "Starting development server..."
python scripts/repair.py
