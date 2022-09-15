from pickle import EMPTY_LIST
from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class Size(models.Model):
    """A size that can be ordered."""
    SIZES = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )

    title = models.CharField(max_length=20, choices=SIZES)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title


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


class Pizza(models.Model):
    """A pizza that can be ordered."""

    size = models.ForeignKey(Size, on_delete=models.CASCADE, default=2, null=False)
    toppings = MultiSelectField(max_length=100, choices=TOPPINGS, null=False, blank=False, default=EMPTY_LIST, max_choices=3)

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.size} pizza with {self.toppings}"


class Cart(models.Model):
    """A pizza that can be ordered."""

    size = models.ForeignKey(Size, on_delete=models.CASCADE, default=2, null=False)
    toppings = MultiSelectField(max_length=100, choices=TOPPINGS, null=False, blank=False, default=EMPTY_LIST, max_choices=3)

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.size} pizza with {self.toppings}"
