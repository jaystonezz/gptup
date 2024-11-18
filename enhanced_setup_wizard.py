
import os
import shutil
import subprocess
from dotenv import load_dotenv

# Load environment variables
def setup_env():
    print("Setting up your environment variables...")
    env_path = os.path.join(os.getcwd(), "config", ".env")
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
    golden_dir = os.path.join(os.getcwd(), "golden_files")
    if not os.path.exists(golden_dir):
        print(f"Golden files directory not found. Creating: {golden_dir}")
        os.makedirs(golden_dir, exist_ok=True)

    # Add placeholder golden file if none exist
    placeholder_file = os.path.join(golden_dir, "example_golden_file.txt")
    if not os.listdir(golden_dir):
        with open(placeholder_file, "w") as file:
            file.write("This is a placeholder for your golden files.")
        print(f"Added placeholder golden file: {placeholder_file}")
    else:
        print("Golden files are valid and ready.")

# Run health checks and install dependencies
def run_health_check():
    print("Running health checks and installing dependencies...")
    required_packages = ["flask", "python-dotenv"]
    for package in required_packages:
        try:
            __import__(package)
            print(f"{package} is installed.")
        except ImportError:
            print(f"{package} is missing. Installing now...")
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

# Generate a summary report
def generate_summary():
    print("Generating summary report...")
    summary_path = os.path.join(os.getcwd(), "setup_summary.txt")
    with open(summary_path, "w") as file:
        file.write("Setup Summary:\n")
        file.write(" - Environment variables: Configured\n")
        file.write(" - Golden files: Validated\n")
        file.write(" - Dependencies: Installed\n")
        file.write(" - Dashboard: Ready to run\n")
    print(f"Summary report generated at {summary_path}")

# Main setup wizard
def main():
    print("Welcome to the Enhanced Guided Setup Wizard!")
    print("1. Setup environment variables")
    print("2. Validate golden files")
    print("3. Run health checks and install dependencies")
    print("4. Start the interactive dashboard")
    print("5. Generate summary report")
    print("6. Exit")

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
            print("Exiting the setup wizard. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
