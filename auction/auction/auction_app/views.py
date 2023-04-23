from django.shortcuts import render, redirect, get_object_or_404
from .models import item
from .forms import *

def index(request):
    items = item.objects.filter().order_by('-create_time')    
    return render(request, 'index.html', {'items': items})

def detail(request, items_id):
    item = get_object_or_404(item, pk=items_id)
    return render(request, 'detail.html', {'item':item })

def add_item(request):
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = itemForm()
        return render(request, 'add_item.html', {'form':form})
