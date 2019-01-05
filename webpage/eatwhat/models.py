# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SeasonalIngredients(models.Model):
    name = models.CharField(max_length=10)
    month = models.IntegerField()
    category = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seasonal_ingredients'

    def __str__(self):
        return self.name
