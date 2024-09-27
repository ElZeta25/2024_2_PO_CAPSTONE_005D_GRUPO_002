from django.conf import settings
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    def __str__(self):
        return self.nombre

class OrderItem(models.Model):
    item= models.ForeignKey(Producto,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Orden(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)
    start_date=models.DateTimeField(auto_now_add=True)
    ordened_date=models.DateTimeField()
    ordened = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username








