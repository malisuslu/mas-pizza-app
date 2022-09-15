from django import forms
from pizzaapp.models import Cart, Pizza

class PizzaForm(forms.ModelForm):
    """Form for ordering a pizza."""

    class Meta:
        model = Cart
        fields = '__all__'

        widgets = {
            'size': forms.Select(attrs={'class': 'w-full border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-green-500'}),
            'toppings': forms.CheckboxSelectMultiple(attrs={'class': 'border rounded py-2 px-2 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-white'}),
        }
