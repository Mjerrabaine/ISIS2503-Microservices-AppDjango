from django.db import models

class Hospital(models.Model):
    activofijo = models.IntegerField(null=False, default=None)
    precio = models.FloatField(null=True, blank=True, default=None)
    marca = models.CharField(max_length=50)
    numquejas = models.FloatField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)