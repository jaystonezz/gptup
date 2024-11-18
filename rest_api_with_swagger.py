
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields

app = Flask(__name__)

# Integrate Flask-RESTx for OpenAPI support
api = Api(app, version='1.0', title='ChatGPT Assistant API',
          description='A mobile-ready API for project setup, repair, and chatbot interactions')

# Define models for input/output
chat_model = api.model('Chat', {
    'question': fields.String(required=True, description="The user's question")
})

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Echo endpoint
@app.route('/api/echo', methods=['POST'])
def echo_input():
    data = request.json
    if not data:
        return jsonify({"error": "No input provided"}), 400
    return jsonify({"your_input": data}), 200

@api.route('/api/chat')
class ChatbotResource(Resource):
    @api.expect(chat_model)
    def post(self):
        data = api.payload
        question = data.get('question', '').lower()
        if "repair" in question:
            return {"answer": "To repair, run the repair script in Boss mode."}, 200
        elif "setup" in question:
            return {"answer": "Use the start_project.sh script to set up your environment."}, 200
        else:
            return {"answer": "I am here to help! Please ask about features or setup."}, 200

@api.route('/api/task')
class TaskSuggestionsResource(Resource):
    def get(self):
        tasks = [
            "Run the repair script in Boss mode.",
            "Use the goodies folder for advanced features.",
            "Check the logs for repair history."
        ]
        return {"suggested_tasks": tasks}, 200

# Register API namespace
api.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
