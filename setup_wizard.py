
import os
import shutil
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

# Run health checks
def run_health_check():
    print("Running health checks...")
    # Check if Python dependencies are installed
    try:
        import flask
        import dotenv
        print("Dependencies are installed.")
    except ImportError as e:
        print(f"Missing dependency: {e}. Please install it using pip.")

# Main setup wizard
def main():
    print("Welcome to the Guided Setup Wizard!")
    print("1. Setup environment variables")
    print("2. Validate golden files")
    print("3. Run health checks")
    print("4. Exit")

    while True:
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            setup_env()
        elif choice == "2":
            validate_golden_files()
        elif choice == "3":
            run_health_check()
        elif choice == "4":
            print("Exiting the setup wizard. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
