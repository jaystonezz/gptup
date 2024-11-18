
import os
import shutil

# Set up sandbox environment
def setup_sandbox():
    print("Setting up Sandbox Mode...")
    sandbox_dir = os.path.join(os.getcwd(), "sandbox_environment")
    if not os.path.exists(sandbox_dir):
        os.makedirs(sandbox_dir, exist_ok=True)
        print(f"Sandbox directory created at: {sandbox_dir}")
    else:
        print(f"Sandbox directory already exists at: {sandbox_dir}")

    # Copy golden files to sandbox
    golden_dir = os.path.join(os.getcwd(), "golden_files")
    if os.path.exists(golden_dir):
        sandbox_golden_dir = os.path.join(sandbox_dir, "golden_files")
        shutil.copytree(golden_dir, sandbox_golden_dir, dirs_exist_ok=True)
        print(f"Golden files copied to sandbox: {sandbox_golden_dir}")
    else:
        print("No golden files found to copy into sandbox.")

    return sandbox_dir

# Run sandbox task
def run_sandbox_task(task_name):
    sandbox_dir = setup_sandbox()
    print(f"Running task '{task_name}' in sandbox: {sandbox_dir}")
    # Simulate a sandbox task
    with open(os.path.join(sandbox_dir, "sandbox_log.txt"), "a") as log_file:
        log_file.write(f"Task {task_name} executed in sandbox.\n")
    print(f"Task '{task_name}' logged in sandbox.")

if __name__ == "__main__":
    run_sandbox_task("Example Sandbox Task")
