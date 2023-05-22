from marshmallow import Schema, fields

class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    operation_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    amount = fields.Float(required=True)
    user_balance = fields.Float(required=True)
    operation_response = fields.Str(required=True)
    date = fields.DateTime(required=True)
