from django.db import models
from emailer import fields as custom_fields
# Create your models here.



class DefaultModel(models.Model):
    dict = custom_fields.DictionaryField('A dictionary of additional information', blank=False, null=False, editable=False)
    
    
    