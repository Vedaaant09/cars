from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to='media/',default='C:/Users/HP/Desktop/python/car_site/car_site/media')
    description = models.TextField()

    def __str__(self):
        return self.name

