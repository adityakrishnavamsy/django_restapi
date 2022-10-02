# to tell that this is a model file we need to import model class in this file 
from django.db import models 

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=600)

    #to change the representation of objects in admin page 
    def __str__(self):
        return self.name + " " + self.description 