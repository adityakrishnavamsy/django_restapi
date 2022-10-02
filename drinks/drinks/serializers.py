from rest_framework import serializers
from .models import Drink
class DrinkSerializer(serializers.ModelSerializer):
    #the meta data of model is containedi in this class 
    class Meta: 
        model = Drink
        fields = ['id' , 'name' , 'description']