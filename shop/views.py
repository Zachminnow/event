from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from shop.forms import SellForm, VendorForm
from django.contrib import messages
from shop.models import SellModel
from django.urls import reverse


# Create your views here.
def dashboard(request):
    products = SellModel.objects.all().order_by('-id')

    vendor_name = request.GET.get('vendor.name')
    if vendor_name:
        products = products.filter(vendor__name__icontains=vendor_name)

    context = {
        'products': products,
        'vendor_query': vendor_name,
    }
    return render(request, 'shop/dashboard.html', context)


def product_detail(request, pk):
    product = get_object_or_404(SellModel, id=pk)
    return render(request, 'shop/product_detail.html', {'product': product})
def sell_view(request):

    if request.method == "POST":
        form = SellForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = SellForm()
    return render(request, 'shop/sell.html', {'form': form})


def vendor_view(request):
    if request.method == "POST":
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vendor created successfully!")
            return redirect(reverse('sell'))

    else:
        form = VendorForm()
    return render(request, 'shop/vendor.html', {'form': form})
