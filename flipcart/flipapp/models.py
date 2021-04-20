from django.db import models

# Create your models here.
class product(models.Model):
    item_id=models.IntegerField()
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='picture')
