import json
from .models import DynamicInputsDatas

def save_to_db(data: dict):
    json_data = json.dumps(data)
    inst = DynamicInputsDatas(data=json_data)
    inst.save()
