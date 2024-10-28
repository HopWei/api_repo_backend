from flask import Flask
from app.config import app, db
from app.routes.task_routes import task_bp

db.create_all()
app.register_blueprint(task_bp, url_prefix='/api')