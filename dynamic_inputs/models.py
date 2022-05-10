from flask import url_for
from core.db import db
from sqlalchemy.dialects.postgresql import JSONB


class DynamicEntry(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    json = db.Column(JSONB)

    def get_absolute_url(self):
        return url_for('dynamic_inputs.detail', id=self.id)
