from flask import Flask, request, jsonify

app = Flask(__name__)

<<<<<<< HEAD
tasks = []
=======
tasks = [{"name": "Ayush Singh Internal Competency Change"}]
>>>>>>> 8f4b214 (updated app.py)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    tasks.append(task)
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

