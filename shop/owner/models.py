from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    price = models.IntegerField()
    purchasing_status = models.BooleanField(default=False)
    date_of_purchase = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    def get_absolute_url(self):
        return reverse('product_detail.html', args=(self.pk, ))