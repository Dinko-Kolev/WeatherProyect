from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def get_id(self):
        return str(self.id)
