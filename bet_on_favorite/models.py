from django.db import models


class FavoriteBetAnalytic(models.Model):
    match = models.CharField(max_length=50)
    coefficient = models.FloatField()
    result = models.CharField(max_length=10)
