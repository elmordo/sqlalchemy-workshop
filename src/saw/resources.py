from flask import Blueprint
from flask_restful import Api, Resource

bp = Blueprint("blueprint", __name__)
api = Api(bp)


class TaskGroups(Resource):

    def get(self):
        pass

    def post(self):
        pass


class TaskGroup(Resource):

    def get(self, group_id):
        pass

    def put(self, group_id):
        pass

    def delete(self, group_id):
        pass


class Tasks(Resource):

    def get(self, group_id):
        pass

    def post(self, group_id):
        pass


class Task(Resource):

    def get(self, group_id, task_id):
        pass

    def put(self, group_id, task_id):
        pass

    def delete(self, group_id, task_id):
        pass


api.add_resource(TaskGroups, "/")
api.add_resource(TaskGroup, "/<int:group_id>")
api.add_resource(Tasks, "/<int:group_id>/task")
api.add_resource(Task, "/<int:group_id>/task/<int:task_id>")
