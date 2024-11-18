
import os
import json
import subprocess
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from tqdm import tqdm
import shutil
import time

# Global Paths
CONFIG_DIR = os.path.join(os.getcwd(), "config")
GOLDEN_DIR = os.path.join(os.getcwd(), "golden_files")
SANDBOX_DIR = os.path.join(os.getcwd(), "sandbox_environment")
FEEDBACK_DIR = os.path.join(os.getcwd(), "logs", "feedback")
LOGS_DIR = os.path.join(os.getcwd(), "logs")
BETA_FEATURES_PATH = os.path.join(CONFIG_DIR, "beta_features.json")

# Helper Functions
def load_feature_toggles():
    if not os.path.exists(BETA_FEATURES_PATH):
        return {}
    with open(BETA_FEATURES_PATH, 'r') as file:
        return json.load(file).get("feature_toggles", {})

def setup_env():
    print("Setting up environment variables...")
    env_path = os.path.join(CONFIG_DIR, ".env")
    if not os.path.exists(env_path):
        os.makedirs(CONFIG_DIR, exist_ok=True)
        with open(env_path, "w") as file:
            api_key = input("Enter OpenAI API Key: ")
            github_token = input("Enter GitHub Token: ")
            file.write(f"OPENAI_API_KEY={api_key}\nGITHUB_TOKEN={github_token}\n")
        print(f".env file created at {env_path}")
    else:
        print(f"Environment variables already configured in {env_path}")

def validate_golden_files():
    print("Validating golden files...")
    if not os.path.exists(GOLDEN_DIR):
        os.makedirs(GOLDEN_DIR, exist_ok=True)
    placeholder = os.path.join(GOLDEN_DIR, "example_golden_file.txt")
    if not os.listdir(GOLDEN_DIR):
        with open(placeholder, "w") as file:
            file.write("This is a placeholder for golden files.")
        print(f"Placeholder golden file created at {placeholder}")

def run_health_check():
    print("Running health checks...")
    required_packages = ["flask", "python-dotenv", "tqdm"]
    for package in tqdm(required_packages, desc="Checking dependencies"):
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call(["pip", "install", package])
    print("All dependencies are installed.")

def setup_sandbox():
    print("Setting up Sandbox Environment...")
    if not os.path.exists(SANDBOX_DIR):
        os.makedirs(SANDBOX_DIR, exist_ok=True)
        print(f"Sandbox directory created at {SANDBOX_DIR}")
    if os.path.exists(GOLDEN_DIR):
        sandbox_golden = os.path.join(SANDBOX_DIR, "golden_files")
        shutil.copytree(GOLDEN_DIR, sandbox_golden, dirs_exist_ok=True)
        print(f"Golden files copied to sandbox: {sandbox_golden}")

def execute_task(task_name, sandbox=False):
    if sandbox:
        setup_sandbox()
        log_file = os.path.join(SANDBOX_DIR, "sandbox_log.txt")
    else:
        log_file = os.path.join(LOGS_DIR, "task_log.txt")
        if not os.path.exists(LOGS_DIR):
            os.makedirs(LOGS_DIR, exist_ok=True)
    print(f"Executing task '{task_name}'...")
    time.sleep(2)
    with open(log_file, "a") as file:
        file.write(f"Task '{task_name}' completed.\n")
    print(f"Task '{task_name}' logged at {log_file}")

# Flask App
app = Flask(__name__)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/run_task', methods=['POST'])
def api_run_task():
    task_name = request.json.get("task_name", "Default Task")
    execute_task(task_name)
    return jsonify({"message": f"Task '{task_name}' executed successfully."}), 200

@app.route('/api/view_feedback', methods=['GET'])
def api_view_feedback():
    feedback_path = os.path.join(FEEDBACK_DIR, "feedback.txt")
    if not os.path.exists(feedback_path):
        return jsonify({"feedback": []}), 200
    with open(feedback_path, "r") as file:
        feedback = file.readlines()
    return jsonify({"feedback": feedback}), 200

# Main Controller
def main():
    print("1. Setup Environment Variables")
    print("2. Validate Golden Files")
    print("3. Run Health Check")
    print("4. Start Sandbox Mode")
    print("5. Start Dashboard")
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
            execute_task("Sandbox Task", sandbox=True)
        elif choice == "5":
            subprocess.Popen(["python", "-m", "flask", "run"])
            print("Dashboard running at http://127.0.0.1:5000/dashboard")
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
