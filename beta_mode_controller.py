
import json
import os
import subprocess

# Paths
CONFIG_DIR = os.path.join(os.getcwd(), "config")
BETA_FEATURES_PATH = os.path.join(CONFIG_DIR, "beta_features.json")
SANDBOX_SCRIPT = os.path.join(os.getcwd(), "scripts", "sandbox_mode.py")
LIVE_PREVIEW_SCRIPT = os.path.join(os.getcwd(), "scripts", "live_preview_system.py")
FEEDBACK_DIR = os.path.join(os.getcwd(), "logs", "feedback")

# Load feature toggles
def load_feature_toggles():
    with open(BETA_FEATURES_PATH, 'r') as file:
        return json.load(file)['feature_toggles']

# Run sandbox mode
def run_sandbox_mode():
    print("Running Sandbox Mode...")
    subprocess.call(["python", SANDBOX_SCRIPT])

# Run live preview system
def run_live_preview():
    print("Running Live Preview System...")
    subprocess.call(["python", LIVE_PREVIEW_SCRIPT])

# View feedback
def view_feedback():
    print("User Feedback:")
    feedback_file = os.path.join(FEEDBACK_DIR, "feedback.txt")
    if os.path.exists(feedback_file):
        with open(feedback_file, "r") as file:
            feedback = file.readlines()
        for line in feedback:
            print(f" - {line.strip()}")
    else:
        print("No feedback available yet.")

# Beta Mode Controller
def beta_mode_controller():
    print("Welcome to Beta Mode!")
    toggles = load_feature_toggles()
    print("Feature Toggles:", toggles)
    print("1. Run Sandbox Mode (Isolated Environment)")
    print("2. Run Live Preview System")
    print("3. View User Feedback")
    print("4. Exit")

    while True:
        choice = input("Enter your choice: ").strip()
        if choice == "1" and toggles.get("sandbox_mode", False):
            run_sandbox_mode()
        elif choice == "2" and toggles.get("live_preview", False):
            run_live_preview()
        elif choice == "3" and toggles.get("feedback_collection", False):
            view_feedback()
        elif choice == "4":
            print("Exiting Beta Mode. Goodbye!")
            break
        else:
            print("Invalid choice or feature is disabled. Please try again.")

if __name__ == "__main__":
    beta_mode_controller()
