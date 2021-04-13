from marshmallow import Schema
from marshmallow.fields import DateTime, Integer, String


class TaskGroupSchema(Schema):
    id = Integer(dump_only=True)
    name = String(required=True)
    comment = String(required=True, allow_none=True)
    color = String(required=True)
    created_at = DateTime(dump_only=True)


class TaskSchema(Schema):
    id = Integer(dump_only=True)
    task_group_id = Integer(dump_only=True)
    name = String(required=True)
    comment = String(required=True, allow_none=True)
    created_at = DateTime(dump_only=True)
    completed_at = DateTime(required=True, allow_none=True)
