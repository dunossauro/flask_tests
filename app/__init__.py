from flask import Flask, request, jsonify, abort

tasks_queue = []

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/send_task', methods=['PUT'])
def put_todo():
    data = request.json
    if 'task' in data:
        tasks_queue.append(data['task'])

        return jsonify('Aceppted'), 201

    abort(300, 'Você não enviou a task')
