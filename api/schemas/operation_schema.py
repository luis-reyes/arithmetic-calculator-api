from marshmallow import Schema, fields

class OperationSchema(Schema):
    id = fields.Int(dump_only=True)
    type = fields.Str(required=True)
    cost = fields.Float(required=True)
