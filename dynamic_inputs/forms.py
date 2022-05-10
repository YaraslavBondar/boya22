from flask_wtf import FlaskForm
from wtforms import StringField, FieldList
from wtforms.validators import DataRequired


class DynamicForm(FlaskForm):

    name = FieldList(StringField('name', validators=[DataRequired()]), min_entries=1)
