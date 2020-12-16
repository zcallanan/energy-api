from django.db import models

# Create your models here.

class Yield(models.Model):
    pv_yield = models.IntegerField(blank=True, null=True, db_column='yield')
    state = models.CharField(primary_key=True, max_length = 2)

    class Meta:
        db_table = 'Yield'

class PostalCode(models.Model):
    plz = models.TextField(primary_key=True)
    state = models.ForeignKey('Yield', models.DO_NOTHING, db_column='state', blank=True, null=True)

    class Meta:
        db_table = 'PostalCode'
