from core.db import db
from sqlalchemy.dialects.postgresql import JSONB


class DynamicEntry(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    json = db.Column(JSONB)

