from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import DynamicInputs
from .models import DynamicInputsDatas


def dynamic_inputs(request):
    template = 'dynamic_inputs/add.html'
    form = DynamicInputs()
    if request.method == 'POST':
        if 'submit' in request.POST:
            form = DynamicInputs(request.POST)
            if form.is_valid():
                inst = DynamicInputsDatas(data=form.cleaned_data)
                inst.save()
                return redirect(reverse('list'))
        if 'add_input' in request.POST:
            form = DynamicInputs(request.POST, add_new_input=True)
    context = {'form': form, }
    return render(request, template, context=context)

def data_list(request):
    template = 'dynamic_inputs/list.html'
    datas = DynamicInputsDatas.objects.all()
    context = {
        'datas': datas,
    }
    return render(request, template, context=context)


def concrete_data(request, id: int):
    data = get_object_or_404(DynamicInputsDatas, id=id)
    return JsonResponse(data.data)
