import uuid
from django.shortcuts import render, redirect
from pizzaapp.forms import PizzaForm
from django.views.generic import TemplateView
from django.contrib.messages.views import messages
from pizzaapp.models import Pizza
from django.template.response import TemplateResponse

# Create your views here.

class home(TemplateView):
    """Home page."""
    template_name = 'pizzaapp/home.html'



def add(request):
    """Add to cart."""
    cart = Pizza.objects.filter(is_ordered=False)

    if request.POST.get('addToCart') == 'Add to Cart':
        form = PizzaForm(request.POST)
        if form.is_valid():
            # assign selected toppings to variables topping1, topping2, and topping3 and save them to the database if they are selected
            form.cleaned_data["id"] = str(uuid.uuid4())
            size = form.cleaned_data['size']
            if len(form.cleaned_data['toppings']) > 3:
                messages.error(request, 'You can only select up to 3 toppings!')
            else:
                topping1 = form.cleaned_data['toppings'][0] if len(form.cleaned_data['toppings']) > 0 else None
                topping2 = form.cleaned_data['toppings'][1] if len(form.cleaned_data['toppings']) > 1 else None
                topping3 = form.cleaned_data['toppings'][2] if len(form.cleaned_data['toppings']) > 2 else None
                Pizza.objects.create(size=size, topping1=topping1, topping2=topping2, topping3=topping3, is_ordered=False)
            messages.success(request, 'Pizza added to cart!')

    elif request.POST.get('submit') == 'Checkout':
        for item in cart:
            item.is_ordered = True
            item.save()
        form = PizzaForm()
        messages.success(request, 'Your order has been submitted!')
        return redirect('add')

    elif request.POST.get('remove') != None:
        Pizza.objects.filter(id=request.POST.get('remove')).delete()
        messages.success(request, 'Pizza removed from cart!')
        
    elif request.POST.get('clear') == 'Clear All':
        Pizza.objects.all().delete()
        
    form = PizzaForm()
    

    context = {
        'form': form,
        'cart': cart,
    }
    return TemplateResponse(request, 'pizzaapp/add.html', context)
