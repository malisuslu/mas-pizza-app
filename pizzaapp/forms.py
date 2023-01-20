from django import forms
from pizzaapp.models import Pizza

class PizzaForm(forms.ModelForm):
    """Form for ordering a pizza."""
    size = forms.ChoiceField(choices=Pizza.SIZES, widget=forms.Select(attrs={'class': 'w-full border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-green-500'})
    )
    toppings = forms.MultipleChoiceField(choices=Pizza.TOPPINGS, widget=forms.CheckboxSelectMultiple(attrs={'class': 'border rounded py-2 px-2 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-white'}))

    class Meta:
        model = Pizza
        fields = ('size', 'toppings')
        labels = {
            'size': 'Size',
            'toppings': 'Toppings',
        }

        # widgets = {
        #     'size': forms.Select(attrs={'class': 'w-full border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-green-500'}),
        #     'toppings': forms.CheckboxSelectMultiple(attrs={'class': 'border rounded py-2 px-2 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-white'}),
        # }
