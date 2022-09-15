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
            form.save()
            form.cleaned_data["id"] = str(uuid.uuid4())
            form = PizzaForm()
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
        form = PizzaForm()
        messages.success(request, 'Pizza removed from cart!')
        
    elif request.POST.get('clear') == 'Clear All':
        Pizza.objects.all().delete()
        form = PizzaForm()

    else:
        form = PizzaForm()

    context = {
        'form': form,
        'cart': cart,
    }
    return TemplateResponse(request, 'pizzaapp/add.html', context)
