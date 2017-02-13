from django.shortcuts import render
from project.models import Gujang, Block, Blockview
# Create your views here.

def gujang_list(request):
    name_select = request.GET.get('name_select', '')
    name_set = Gujang.objects.all()

    if name_select :
        name_set = name_set.filter(name__icontains=name_select)
    return render(request, 'project/gujang_list.html',{
        'name_select' : name_select,
        'name_set' : name_set,
        })

def gujang_detail(request, id):
    gujang = Gujang.objects.get(id=id)
    return render(request, 'project/gujang_detail.html',{
        'gujang': gujang,
    })

def gujang_main(request):
    return render(request, 'project/yagudjango_main.html')