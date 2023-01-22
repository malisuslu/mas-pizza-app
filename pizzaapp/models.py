from pickle import EMPTY_LIST
from django.db import models


class Pizza(models.Model):
    """A pizza that can be ordered."""

    size = models.CharField(max_length=10, null=False, blank=False, default='Small')
    topping1 = models.CharField(max_length=20, null=True, blank=True)
    topping2 = models.CharField(max_length=20, null=True, blank=True)
    topping3 = models.CharField(max_length=20, null=True, blank=True)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.size} pizza with {self.topping1}, {self.topping2}, {self.topping3}"


# class Cart(Pizza):
#     """A cart that can be ordered."""

#     def __str__(self):
#         """Return a string representation of the model."""
#         return f"{self.size} pizza with {self.toppings}"