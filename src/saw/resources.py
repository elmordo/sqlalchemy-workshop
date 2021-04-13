from flask import Blueprint, current_app, request
from flask_restful import Api, Resource, abort
from saw import model
from saw.schemas import TaskGroupSchema
from sqlalchemy.orm import Session
from werkzeug.routing import ValidationError

bp = Blueprint("blueprint", __name__)
api = Api(bp)


class TaskGroups(Resource):

    def get(self):
        session: Session = current_app.session_maker()
        groups = session.query(model.TaskGroup).all()
        schema = TaskGroupSchema(many=True)
        return schema.dump(groups)

    def post(self):
        schema = TaskGroupSchema()
        try:
            data = schema.load(request.json)
        except ValidationError:
            abort(400)
        group = model.TaskGroup()
        group.fill_data(data)

        session: Session = current_app.session_maker()
        session.add(group)
        session.commit()
        return schema.dump(group)


class TaskGroup(Resource):

    def get(self, group_id):
        session: Session = current_app.session_maker()
        group = session.query(model.TaskGroup).get(group_id)
        # group = session.query(model.TaskGroup).filter(model.TaskGroup.id == group_id).first()  # same as query with .get() method
        if group is None:
            abort(404)
        schema = TaskGroupSchema()
        return schema.dump(group)

    def put(self, group_id):
        session: Session = current_app.session_maker()
        group: model.TaskGroup = session.query(model.TaskGroup).get(group_id)
        if group is None:
            abort(404)
        schema = TaskGroupSchema()
        try:
            data = schema.load(request.json)
        except ValidationError:
            abort(400)
        group.fill_data(data)
        session.commit()
        return schema.dump(group)

    def delete(self, group_id):
        session: Session = current_app.session_maker()
        group: model.TaskGroup = session.query(model.TaskGroup).get(group_id)
        if group is None:
            abort(404)
        session.delete(group)
        session.commit()


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
