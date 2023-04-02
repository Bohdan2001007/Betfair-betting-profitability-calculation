from django.db import models


class ScoreAnalytic(models.Model):
    match = models.CharField(max_length=50)
    score = models.CharField(max_length=10)
    coefficient = models.FloatField()
    result = models.CharField(max_length=10)
