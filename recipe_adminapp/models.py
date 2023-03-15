from django.db import models

# Create your models here.
class Recipedb(models.Model):
    recipe_name=models.CharField(max_length=50)
    recipe_image=models.ImageField(upload_to='sample',default='null.jpg')
    instruction=models.CharField(max_length=100)
    ingredients=models.CharField(max_length=100)
