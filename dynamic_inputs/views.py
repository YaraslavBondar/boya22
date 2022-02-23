from django.http import JsonResponse
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)

from .forms import DynamicInputs
from .models import DynamicInputsDatas
from .utils import process_form_data, save_to_db


def dynamic_inputs(request):
    template = 'dynamic_inputs/add.html'
    form = DynamicInputs()
    if request.method == 'POST':
        form = DynamicInputs(request.POST)
        if form.is_valid():
            data = process_form_data(request)
            save_to_db(data)
            return redirect('list')
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
    data = get_object_or_404(DynamicInputsDatas, id=id)
    return JsonResponse(data.data)
