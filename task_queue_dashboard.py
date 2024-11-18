
from flask import Flask, render_template, request, jsonify
import threading
import time

app = Flask(__name__)

# Global task queue and statuses
tasks = []
task_status = {}

# Task executor thread
def task_executor():
    while True:
        if tasks:
            task_id = tasks.pop(0)
            task_status[task_id] = "In Progress"
            time.sleep(5)  # Simulate task execution
            task_status[task_id] = "Completed"
        time.sleep(1)

# Start the task executor thread
executor_thread = threading.Thread(target=task_executor, daemon=True)
executor_thread.start()

# Route to add a task to the queue
@app.route('/api/add_task', methods=['POST'])
def add_task():
    task_id = f"task-{len(task_status) + 1}"
    tasks.append(task_id)
    task_status[task_id] = "Pending"
    return jsonify({"message": f"Task {task_id} added successfully!"}), 200

# Route to fetch the status of all tasks
@app.route('/api/task_status', methods=['GET'])
def get_task_status():
    return jsonify(task_status), 200

# Dashboard route
@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard_with_tasks.html', task_status=task_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
