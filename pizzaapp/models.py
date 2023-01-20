from pickle import EMPTY_LIST
from django.db import models
from multiselectfield import MultiSelectField

class Pizza(models.Model):
    """A pizza that can be ordered."""

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

    size = models.CharField(max_length=10, null=False, blank=False)
    toppings = MultiSelectField(max_length=100, choices=TOPPINGS, null=False, blank=False, default=EMPTY_LIST, max_choices=3)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.size} pizza with {self.toppings}"


# class Cart(Pizza):
#     """A cart that can be ordered."""

#     def __str__(self):
#         """Return a string representation of the model."""
#         return f"{self.size} pizza with {self.toppings}"