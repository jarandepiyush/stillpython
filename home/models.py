from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()
    desc = models.CharField(max_length=30)
    date = models.DateField( auto_now=False, auto_now_add=False)
