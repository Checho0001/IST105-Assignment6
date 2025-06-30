from django.db import models

# Create your models here.
class Bitwise(models.Model):
    original = models.JSONField()
    sorted_over_10 = models.JSONField()
    average = models.FloatField()
    count_positive = models.IntegerField()
    even_odd = models.JSONField()
    warnings = models.JSONField()

    def __str__(self):
        return f"Bitwise Result (Avg: {self.average}, Pos: {self.count_positive})"
