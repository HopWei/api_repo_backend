from app.models.task_model import Task
from app.config import db

class TaskRepository:
    def get_all_tasks():
        return Task.query.all()
    
    def get_task_by_id(task_id):
        return Task.query.get(task_id)
    
    def add_task(task):
        db.session.add(task)
        db.session.commit()

    def delete_task(task):
        db.session.delete(task)
        db.session.commit()
    
    def update_task(task):
        db.session.commit()