from django.db import models

class contact(models.Model):
    name=models.CharField(max_length=20)
    number=models.CharField(max_length=10)
    

    def __str__(self) :
        return self.name



# Create your models here.
