from core.db import db
from sqlalchemy.dialects.postgresql import JSONB


class FormData(db.Model):

    __tablename__ == 'form_data'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSONB)
