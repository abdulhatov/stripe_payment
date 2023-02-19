from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0) #cent

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)