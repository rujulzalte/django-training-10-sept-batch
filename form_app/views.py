from django.http import JsonResponse
from django.shortcuts import render
from .forms import ProductForm
from .models import Product

# Create your views here.

def product_upload_form(request):
    if request.method == 'POST':
        try:
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                # product = Product(name=form.cleaned_data['name'], file=form.cleaned_data['file'])
                # product.save()
                form.save()
                return JsonResponse({'message': 'Product uploaded successfully'})
            else:
                return JsonResponse({'error': form.errors})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
    else:
        form = ProductForm()
    return render(request, 'form_app/product.html', {'form': form})