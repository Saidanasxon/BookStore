from django.db import models
from sellers.models import Book
from users.models import User

class Cart(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.book.title
    
    @property
    def total_price(self):
        return self.book.price * self.quantity
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)  

    @property
    def total_price(self):
        return self.book.price * self.quantity