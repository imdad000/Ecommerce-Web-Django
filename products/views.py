from django.shortcuts import render,get_object_or_404
from django.http import Http404
# Create your views here.
from . models import Product
from django.shortcuts import render, get_object_or_404

def product_view(request):
	query_set=Product.objects.all()
	context={
			'p_list':query_set
		}
	return render(request,'products/product_list.html', context)


def product_detail_view(request, pk=None, *args, **kwargs):
    try:
    #instance = Product.objects.get(pk=pk) 
    instance = get_object_or_404(Product, pk=pk)
    except Product.DoesNotExist:
        print('no product here')
        raise Http404("Product doesn't exist")
    except:
        print("huh?")

    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)

