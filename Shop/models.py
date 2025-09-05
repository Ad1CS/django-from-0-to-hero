from django.db import models

class Product(models.Model):
    Title=models.CharField(max_length= 20)
    Img=models.ImageField(upload_to="media")
    Price=models.DecimalField(max_digits=6,decimal_places=2)
    Content=models.TextField()
    Time_created=models.DateTimeField(auto_now_add=True)
    Last_update=models.DateTimeField(auto_now=True)
    Stock=models.BooleanField()







