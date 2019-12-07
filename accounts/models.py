from django.db import models

# Create your models here.

class Accounts(models.Model):
    name = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=30, decimal_places=3)
    email = models.EmailField()

    def __str__(self):
        return self.name

