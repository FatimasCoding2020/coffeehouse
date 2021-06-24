from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=250)
    sku = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, default=0)
    image = models.ImageField(null=True, blank=True, upload_to='static/uploaded_images')
    image_link = models.URLField(max_length=1024, null=True, blank=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
