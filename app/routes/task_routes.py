from flask import Blueprint, jsonify, request
from app.services.task_service import TaskService

task_bp = Blueprint('task', __name__)

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = TaskService.get_all_tasks()
    return jsonify([task.to_dict() for task in tasks])

@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = TaskService.get_task_by_id(task_id)
    return jsonify(task.to_dict()) if task else ('', 404)

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = TaskService.create_task(data)
    return jsonify(task.to_dict()), 201

@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = TaskService.update_task(task_id, data)
    return jsonify(task.to_dict()) if task else ('', 404)

@task_bp.route('/tasks/<int:task_id', methods=['DELETE'])
def delete_task(task_id):
    task = TaskService.delete_task(task_id)
    return ('', 204) if task else ('', 404)