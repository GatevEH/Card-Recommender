from tabnanny import verbose
from django.db import models

class Monster(models.Model):
    c_name = models.CharField(max_length=255)
    c_description = models.CharField(max_length=5000)
    c_race = models.CharField(max_length=255)
    c_attribute = models.CharField(max_length=255)
    c_atk = models.CharField(max_length=255)
    c_def = models.CharField(max_length=255)
    c_type = models.CharField(max_length=255)
    c_level = models.IntegerField()
    class Meta:
        db_table = 'monsters'
