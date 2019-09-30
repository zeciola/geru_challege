from marshmallow import Schema, fields, validate


class UserSessionSchema(Schema):
    id = fields.Integer()
    session_date = fields.Date(required=True)
    session_path = fields.String(required=True, validate=validate.Length(min=2, max=4095))
    session_browser = fields.String(required=True, validate=validate.Length(min=2, max=4095))
    session_timestamp = fields.Float(required=True)
    session_pdtb_id = fields.String(required=True, validate=validate.Length(min=2, max=4095))
