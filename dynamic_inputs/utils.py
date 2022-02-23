from .models import DynamicInputsDatas

def save_to_db(data: dict):
    inst = DynamicInputsDatas(data=data)
    inst.save()
