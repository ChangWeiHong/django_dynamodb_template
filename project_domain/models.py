# from django.db import models

# Create your models here.
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
import os
from dotenv import load_dotenv

load_dotenv()

class YourModel(Model):
    class Meta:
        table_name = "Table"
        region = os.getenv('AWS_REGION', 'default_value')

    tableId = UnicodeAttribute(hash_key=True)
    createdDatetime = UnicodeAttribute()