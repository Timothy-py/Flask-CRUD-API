from flask_restful import Resource
import logging as logger


class TaskById(Resource):

    def get(self, taskId):
        logger.debug("Inside get method of task by Id")
        return {"message": "inside get method of task by Id. TASK-ID={}".format(taskId)}, 200

    def post(self, taskId):
        logger.debug("Inside post method of task by Id")
        return {"message": "inside post method of task by Id. TASK-ID={}".format(taskId)}, 200

    def put(self, taskId):
        logger.debug("Inside put method")
        return {"message": "inside put method of task by Id. TASK-ID={}".format(taskId)}, 200

    def delete(self, taskId):
        logger.debug("Inside delete method")
        return {"message": "inside delete method of task by Id. TASK-ID={}".format(taskId)}, 200
