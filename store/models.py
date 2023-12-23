from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Category_media/', blank=True, null= True)
   

    class Meta:
        
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name

class Card(models.Model):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length= 250)
    price = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=None)
    ordering = models.IntegerField(blank=True, null= True)

    def __str__(self):
            return self.title

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField()
    message = models.CharField(max_length=250)

    def __str__(self):
            return self.first_name
    