from django.db import models
from users.models import User

class BookCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='category_pics/', default='category_pics/category_default.jpg')

    def __str__(self):
        return self.name
    

class BookGenre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='genre_pics/', default=' genre_pics/category_default.jpg')

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.ForeignKey(BookGenre, on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    price = models.PositiveIntegerField()
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='book_pics/', blank=True, null=True, default='')
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, related_name='books')
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    @property
    def total_price(self):
        return self.price * self.quantity

    