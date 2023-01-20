from django import forms
from pizzaapp.models import Pizza

class PizzaForm(forms.ModelForm):
    """Form for ordering a pizza."""

    SIZES = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )

    TOPPINGS = (
        ('pepperoni', 'Pepperoni'),
        ('sausage', 'Sausage'),
        ('bacon', 'Bacon'),
        ('mushrooms', 'Mushrooms'),
        ('onions', 'Onions'),
        ('pineapple', 'Pineapple'),
        ('ham', 'Ham'),
        ('anchovies', 'Anchovies'),
        ('extra cheese', 'Extra Cheese')
    )

    size = forms.ChoiceField(choices=SIZES, widget=forms.Select(attrs={'class': 'w-full border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-green-500'}), help_text='Select a size for your pizza.')
    
    # Create multiple checkboxes for toppings with max of 3 toppings selected and use the toppings list from models.py to populate the checkboxes with the toppings list from models.py
    toppings = forms.MultipleChoiceField(choices=TOPPINGS, widget=forms.CheckboxSelectMultiple(attrs={'class': 'border rounded py-2 px-2 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-white'}))


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
