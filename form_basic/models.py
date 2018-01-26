from django.db import models

# Create your models here.


# Create your models here.
class Reguser(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    addr = models.CharField(max_length=256)
    tel = models.CharField(max_length=128)      
    email = models.EmailField(max_length=254,unique=True)

