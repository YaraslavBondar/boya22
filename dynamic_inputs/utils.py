import json

from .models import DynamicInputsDatas

def process_form_data(request) -> dict:
    data = {
        field: value
        for field, value in request.POST.items()
        if field not in ['csrfmiddlewaretoken', 'submit'] and value
    }
    return data

def save_to_db(data: dict):
    json_data = json.dumps(data)
    inst = DynamicInputsDatas(data=json_data)
    inst.save()
