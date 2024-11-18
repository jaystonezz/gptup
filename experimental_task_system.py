
import json
import time

# Load experimental feature toggles
def load_feature_toggles():
    with open('config/beta_features.json', 'r') as file:
        return json.load(file)['feature_toggles']

# Execute experimental task
def execute_task(task_name):
    print(f"Executing experimental task: {task_name}")
    time.sleep(2)  # Simulate task execution
    print(f"Task {task_name} completed.")

# Run experimental tasks based on toggles
def run_experimental_tasks():
    toggles = load_feature_toggles()
    print("Loaded Feature Toggles:", toggles)
    if toggles.get("live_preview"):
        print("Running Live Preview...")
        execute_task("Live Preview Task")
    if toggles.get("sandbox_mode"):
        print("Running Sandbox Mode Task...")
        execute_task("Sandbox Task")

if __name__ == "__main__":
    run_experimental_tasks()
