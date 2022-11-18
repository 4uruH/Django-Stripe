from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name

    def get_normal_price(self):
        return "{0:.2f}".format(self.price / 100)