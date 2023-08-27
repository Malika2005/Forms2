from django.shortcuts import render, redirect
from .forms import ProductModelForm
from .models import Product


def start_page(request):
    context = {'products': Product.objects.all()}
    return render(request, 'start_page.html', context)

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('owner:start_page')

def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductModelForm(instance=product)
    if request.method == 'POST':
        form = ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('owner:start_page')
    return render(request, 'edit_product.html', {'form': form})

def add_product(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owner:start_page')
    return render(request, 'add_product.html', {'form': form})