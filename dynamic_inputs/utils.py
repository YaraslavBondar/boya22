import json

from core.db import db

from dynamic_inputs.models import DynamicEntry


def prepare_data(form_data: dict):
    tmp = {}
    for key, value in form_data.items():
        if key == 'csrf_token':
            continue
        if isinstance(value, list):
            for num, item in enumerate(value):
                tmp[key+str(num)*(num!=0)] = item
        else:
            tmp[key] = value
    return tmp


def save_to_db(data):
    entry = DynamicEntry(json=data)
    db.session.add(entry)
    db.session.commit()


def get_from_db(id: int):
    return DynamicEntry.query.get(id)


def get_all_from_db():
    return DynamicEntry.query.all()
