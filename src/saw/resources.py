from flask import Blueprint
from flask_restful import Api, Resource

bp = Blueprint()
api = Api(bp)


class TaskGroups(Resource):

    def get(self):
        pass

    def post(self):
        pass


class TaskGroup(Resource):

    def get(self, id_):
        pass

    def put(self, id_):
        pass

    def delete(self, id_):
        pass


class Tasks(Resource):

    def get(self):
        pass

    def post(self):
        pass


class Task(Resource):

    def get(self, id_):
        pass

    def put(self, id_):
        pass

    def delete(self, id_):
        pass
