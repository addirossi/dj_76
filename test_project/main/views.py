from django.http import HttpResponse, Http404
from django.shortcuts import render

from main.models import Product


def index_page(request):
    return HttpResponse('Hello world')


def products_list(request):
    print('CHHEEEECCCKKKK!!!!!!!!')
    products = Product.objects.all()
    print(f'Количество полученных товаров: {products.count()}')
    template_name = 'main/list.html'
    return render(request, template_name, {'products': products})


def product_details(request, product_id):
    try:
        prod = Product.objects.get(id=product_id)
        print(prod.name)
        template_name = 'details.html'
        return render(request, template_name, {'product': prod})
    except Product.DoesNotExist:
        raise Http404('Product not found')
