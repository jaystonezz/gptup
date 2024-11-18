
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Path to save feedback
FEEDBACK_DIR = os.path.join(os.getcwd(), "logs", "feedback")
os.makedirs(FEEDBACK_DIR, exist_ok=True)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard_with_feedback.html')

@app.route('/api/submit_feedback', methods=['POST'])
def submit_feedback():
    feedback = request.json.get("feedback")
    if not feedback:
        return jsonify({"error": "Feedback cannot be empty"}), 400
    feedback_file = os.path.join(FEEDBACK_DIR, "feedback.txt")
    with open(feedback_file, "a") as file:
        file.write(feedback + "\n")
    return jsonify({"message": "Thank you for your feedback!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
