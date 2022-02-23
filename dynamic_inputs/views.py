import json
from django.http import JsonResponse
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)
from django.urls import reverse

from .forms import DynamicInputs
from .models import DynamicInputsDatas
from .utils import save_to_db


def dynamic_inputs(request):
    template = 'dynamic_inputs/add.html'
    form = DynamicInputs()
    if request.method == 'POST':
        if 'submit' in request.POST:
            form = DynamicInputs(request.POST)
            if form.is_valid():
                save_to_db(form.cleaned_data)
                return redirect(reverse('list'))
        if 'add_input' in request.POST:
            form = DynamicInputs(request.POST, add_new_input=True)
    context = {'form': form, }
    return render(request, template, context=context)

def data_list(request):
    template = 'dynamic_inputs/list.html'
    datas = get_list_or_404(DynamicInputsDatas)
    context = {
        'datas': datas,
    }
    return render(request, template, context=context)


def concrete_data(request, id: int):
    obj = get_object_or_404(DynamicInputsDatas, id=id)
    json_data = json.loads(obj.data)
    return JsonResponse(json_data)
