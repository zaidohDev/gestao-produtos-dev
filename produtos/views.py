from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


@login_required
def products_list(request):
    products = Product.objects.all()
    return render(request, 'produtos/products.html', {'products': products})


@login_required
def products_new(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('products_list')
    return render(request, 'produtos/product_form.html', {'form': form})


@login_required
def products_update(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('products_list')
    return render(request, 'produtos/product_form.html', {'form': form})


@login_required
def products_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == 'POST':
        product.delete()
        return redirect('products_list')
    return render(request, 'produtos/product_delete_confirm.html', {'product': product, 'form': form})
