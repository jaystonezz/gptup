
import os
import shutil
import hashlib
import json

# Define the reference structure or "golden" configuration
REFERENCE_FILES = {
    "config/chatgpt_config.json": "golden/chatgpt_config.json",
    "web_dashboard/app.py": "golden/web_dashboard_app.py",
    "scripts/main.py": "golden/main.py",
    "scripts/chatgpt_assistant_cli.py": "golden/chatgpt_assistant_cli.py",
    "scripts/experimental_feature.py": "golden/experimental_feature.py"
}

# Default base directory (/mnt/data)
BASE_DIR = "/mnt/data"
PROJECT_DIR = os.path.join(BASE_DIR, "project")
REFERENCE_DIR = os.path.join(BASE_DIR, "golden_files")

# Structured log file
LOG_FILE = os.path.join(BASE_DIR, "structured_log.json")
log_entries = []

# Calculate file checksum
def calculate_checksum(file_path):
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except FileNotFoundError:
        return None

# Scan and repair files
def scan_and_repair(target_dir):
    updates = []
    for target, reference in REFERENCE_FILES.items():
        target_path = os.path.join(target_dir, target)
        reference_path = os.path.join(REFERENCE_DIR, reference)
        
        if not os.path.exists(reference_path):
            log_entries.append({"file": target, "action": "missing_reference", "status": "skipped"})
            continue

        target_checksum = calculate_checksum(target_path)
        reference_checksum = calculate_checksum(reference_path)
        
        if target_checksum is None:
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            shutil.copy(reference_path, target_path)
            updates.append(f"Added missing file: {target}")
            log_entries.append({"file": target, "action": "add", "status": "success"})
        elif target_checksum != reference_checksum:
            shutil.copy(reference_path, target_path)
            updates.append(f"Updated file: {target}")
            log_entries.append({
                "file": target, 
                "action": "update", 
                "status": "success", 
                "previous_checksum": target_checksum, 
                "new_checksum": reference_checksum
            })
        else:
            log_entries.append({"file": target, "action": "validate", "status": "no_change"})
    
    return updates

# Write structured logs
def write_logs():
    with open(LOG_FILE, "w") as log_file:
        json.dump(log_entries, log_file, indent=4)

# Main execution
if __name__ == "__main__":
    if not os.path.exists(PROJECT_DIR):
        print(f"Project directory {PROJECT_DIR} does not exist. Exiting.")
        exit(1)
    
    updates = scan_and_repair(PROJECT_DIR)
    if updates:
        print("The following files were updated:")
        for update in updates:
            print(f" - {update}")
    else:
        print("All files are up-to-date.")

    write_logs()
    print(f"Log file created at: {LOG_FILE}")
