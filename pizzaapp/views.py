import uuid
from django.shortcuts import render, redirect
from pizzaapp.forms import PizzaForm
from django.views.generic import TemplateView
from django.contrib.messages.views import messages
from pizzaapp.models import Pizza

# Create your views here.

class home(TemplateView):
    """Home page."""
    template_name = 'pizzaapp/home.html'


cart = []
def add(request):
    """Add to cart."""
       
    if request.method == "GET":
        form = PizzaForm()
    
    elif request.POST.get('addToCart') == 'Add to Cart':
        form = PizzaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data["id"] = str(uuid.uuid4())
            cart.append(data)
            return redirect('add')

    elif request.POST.get('submit') == 'Checkout':
        for item in cart:
            Pizza.objects.create(size=item['size'], toppings=item['toppings'])
        cart.clear()
        form = PizzaForm()
        messages.success(request, 'Your order has been submitted!')
        return redirect('add')

    elif request.POST.get('remove') != None:
        for item in cart:
            if item['id'] == request.POST.get('remove'):
                cart.remove(item)
                break
        form = PizzaForm()

    elif request.POST.get('clear') == 'Clear All':
        cart.clear()
        form = PizzaForm()



    context = {
        'form': form,
        'cart': cart,
    }
    return render(request, 'pizzaapp/add.html', context)
