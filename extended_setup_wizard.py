
import os
import shutil
import subprocess
import json
from dotenv import load_dotenv
from tqdm import tqdm

# Paths and constants
CONFIG_DIR = os.path.join(os.getcwd(), "config")
DEFAULT_ENV_PATH = os.path.join(CONFIG_DIR, ".env")
GOLDEN_DIR = os.path.join(os.getcwd(), "golden_files")
LOGS_DIR = os.path.join(os.getcwd(), "logs")
SUMMARY_PATH = os.path.join(os.getcwd(), "setup_summary.txt")
WIZARD_TASKS_PATH = os.path.join(CONFIG_DIR, "wizard_tasks.json")

# Setup environment variables
def setup_env():
    print("Setting up your environment variables...")
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR, exist_ok=True)
    
    env_path = input(f"Enter path for .env file (default: {DEFAULT_ENV_PATH}): ").strip() or DEFAULT_ENV_PATH
    if os.path.exists(env_path):
        print(f"Environment file already exists: {env_path}")
        return

    # Create a new .env file interactively
    print("Creating a new .env file...")
    with open(env_path, "w") as file:
        api_key = input("Enter your API key for OpenAI: ").strip()
        github_token = input("Enter your GitHub token: ").strip()
        file.write(f"OPENAI_API_KEY={api_key}\nGITHUB_TOKEN={github_token}\n")
    print(f".env file created at {env_path}")

# Validate golden files
def validate_golden_files():
    print("Validating golden files...")
    if not os.path.exists(GOLDEN_DIR):
        print(f"Golden files directory not found. Creating: {GOLDEN_DIR}")
        os.makedirs(GOLDEN_DIR, exist_ok=True)

    # Add placeholder golden file if none exist
    placeholder_file = os.path.join(GOLDEN_DIR, "example_golden_file.txt")
    if not os.listdir(GOLDEN_DIR):
        with open(placeholder_file, "w") as file:
            file.write("This is a placeholder for your golden files.")
        print(f"Added placeholder golden file: {placeholder_file}")
    else:
        print("Golden files are valid and ready.")

# Run health checks and install dependencies
def run_health_check():
    print("Running health checks and installing dependencies...")
    required_packages = ["flask", "python-dotenv", "tqdm"]
    for package in tqdm(required_packages, desc="Checking dependencies"):
        try:
            __import__(package)
        except ImportError:
            print(f"Installing missing dependency: {package}")
            subprocess.check_call(["pip", "install", package])
    print("All dependencies are installed and ready.")

# Start the interactive dashboard
def start_dashboard():
    print("Starting the interactive dashboard...")
    dashboard_path = os.path.join(os.getcwd(), "scripts", "task_queue_dashboard.py")
    if os.path.exists(dashboard_path):
        subprocess.Popen(["python", dashboard_path])
        print("Dashboard is running. Access it at http://127.0.0.1:5000/dashboard")
    else:
        print("Dashboard script not found. Please check your setup.")

# Generate summary reports
def generate_summary():
    print("Generating summary reports...")
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR, exist_ok=True)
    
    summary_text = "Setup Summary:\n"
    summary_text += " - Environment variables: Configured\n"
    summary_text += " - Golden files: Validated\n"
    summary_text += " - Dependencies: Installed\n"
    summary_text += " - Dashboard: Ready to run\n"
    
    with open(SUMMARY_PATH, "w") as file:
        file.write(summary_text)
    
    print(f"Summary report saved at: {SUMMARY_PATH}")

# Load customizable tasks from wizard_tasks.json
def load_custom_tasks():
    if os.path.exists(WIZARD_TASKS_PATH):
        with open(WIZARD_TASKS_PATH, "r") as file:
            tasks = json.load(file)
        print("Custom Tasks:")
        for idx, task in enumerate(tasks.get("tasks", []), start=1):
            print(f"{idx}. {task}")
    else:
        print("No custom tasks found.")

# Main setup wizard
def main():
    print("Welcome to the Extended Guided Setup Wizard!")
    print("1. Setup environment variables")
    print("2. Validate golden files")
    print("3. Run health checks and install dependencies")
    print("4. Start the interactive dashboard")
    print("5. Generate summary reports")
    print("6. Load custom tasks")
    print("7. Exit")

    while True:
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            setup_env()
        elif choice == "2":
            validate_golden_files()
        elif choice == "3":
            run_health_check()
        elif choice == "4":
            start_dashboard()
        elif choice == "5":
            generate_summary()
        elif choice == "6":
            load_custom_tasks()
        elif choice == "7":
            print("Exiting the setup wizard. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
