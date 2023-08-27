from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from owner.models import Product

def product_list(request):
    context = {'products': Product.objects.all()}
    return render(request, 'product_list.html', context)

def product_detail(request, pk):
    context = {'product': get_object_or_404(Product, pk=pk)}
    return render(request, 'product_detail.html', context)

def purchase_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.purchasing_status = True
    product.date_of_purchase = timezone.now()
    product.save()
    return redirect('customer:product_list')