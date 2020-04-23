from flask_restful import Api
from .task import Task
from .taskById import TaskById

from app import flaskAppInstance

restServer = Api(flaskAppInstance)

restServer.add_resource(Task, "/api/v1.0/task")
restServer.add_resource(TaskById, "/api/v1.0/task/id/<string:taskId>")