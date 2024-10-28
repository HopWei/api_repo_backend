from app.models.task_model import Task
from app.repositories.task_repository import TaskRepository

class TaskService:
    def get_all_tasks():
        return TaskRepository.get_all_tasks()
    
    def get_task_by_id(task_id):
        return TaskRepository.get_task_by_id(task_id)
    
    def create_task(data):
        task = Task(title=data['title'], description=data['description'])
        TaskRepository.add_task(task)
        return task
    
    def delete_task(task_id):
        task = TaskRepository.get_task_by_id(task_id)
        if task:
            TaskRepository.delete_task(task)
        return task

    def update_task(task_id, data):
        task = TaskRepository.get_task_by_id(task_id)
        if task:
            task.title = data.get('title', task.title)
            task.description = data.get('description', task.description)
            task.completed = data.get('completed', task.completed)
            TaskRepository.update_task(task)
        return task