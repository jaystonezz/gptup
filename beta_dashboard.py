
from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

# Paths to scripts
SANDBOX_SCRIPT = os.path.join(os.getcwd(), "scripts", "sandbox_mode.py")
LIVE_PREVIEW_SCRIPT = os.path.join(os.getcwd(), "scripts", "live_preview_system.py")
FEEDBACK_DIR = os.path.join(os.getcwd(), "logs", "feedback")

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard_with_beta.html')

@app.route('/api/run_sandbox', methods=['POST'])
def run_sandbox():
    subprocess.Popen(["python", SANDBOX_SCRIPT])
    return jsonify({"message": "Sandbox Mode started successfully!"}), 200

@app.route('/api/run_live_preview', methods=['POST'])
def run_live_preview():
    subprocess.Popen(["python", LIVE_PREVIEW_SCRIPT])
    return jsonify({"message": "Live Preview started successfully!"}), 200

@app.route('/api/view_feedback', methods=['GET'])
def view_feedback():
    feedback_file = os.path.join(FEEDBACK_DIR, "feedback.txt")
    feedback = []
    if os.path.exists(feedback_file):
        with open(feedback_file, "r") as file:
            feedback = file.readlines()
    return jsonify({"feedback": feedback}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
