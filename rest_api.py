
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample route: health check
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Sample route: Echo input
@app.route('/api/echo', methods=['POST'])
def echo_input():
    data = request.json
    if not data:
        return jsonify({"error": "No input provided"}), 400
    return jsonify({"your_input": data}), 200

# Chatbot interaction endpoint
@app.route('/api/chat', methods=['POST'])
def chatbot_interaction():
    data = request.json
    question = data.get('question', '').lower() if data else ''
    if "repair" in question:
        return jsonify({"answer": "To repair, run the repair script in Boss mode."})
    elif "setup" in question:
        return jsonify({"answer": "Use the start_project.sh script to set up your environment."})
    else:
        return jsonify({"answer": "I am here to help! Please ask about features or setup."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
