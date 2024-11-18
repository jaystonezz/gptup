
from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)

# Path to logs and health check status
LOG_FILE = "/mnt/data/structured_log.json"

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Dashboard route
@app.route('/dashboard', methods=['GET'])
def dashboard():
    # Read log file
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as log_file:
            logs = json.load(log_file)

    return render_template('dashboard.html', logs=logs)

# Quick action: Run repair
@app.route('/api/run_repair', methods=['POST'])
def run_repair():
    # Placeholder for triggering repair logic
    return jsonify({"message": "Repair task started successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
