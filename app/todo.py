from flask import Blueprint, request, jsonify, abort

tasks_queue = []

app = Blueprint('todo', __name__)


@app.route('/send_task', methods=['PUT'])
def put_task():
    data = request.json
    if 'task' in data:
        tasks_queue.append(data['task'])

        return jsonify('Aceppted'), 201

    abort(400, 'Você não enviou a task')


@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks_queue}), 200


@app.route('/modify_task/<string:old_task>/<string:new_task>', methods=['GET'])
def modify_tasks(old_task, new_task):
    for i, task in enumerate(tasks_queue):
        if old_task == task:
            tasks_queue[i] = new_task
            return jsonify('Aceppted'), 201

    abort(404, 'Task não pode ser modificada, ela não está na lista')
