from django.db import models

# Create your models here.
class Bitwise(models.Model):
    original = models.TextField()
    sorted_over_10 = models.TextField()
    average = models.FloatField()
    count_positive = models.IntegerField()
    even_odd = models.TextField()
    warnings = models.TextField()

    def __str__(self):
        return f"Bitwise Result (Avg: {self.average}, Pos: {self.count_positive})"
