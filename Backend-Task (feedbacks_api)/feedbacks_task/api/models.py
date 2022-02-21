from email.policy import default
from tokenize import blank_re
import black
from django.db import models
from django.forms import TimeField
import datetime

# Create your models here.

class Feedback(models.Model):
    name=models.CharField(max_length=15)
    feed=models.CharField(max_length=50)

    def __str__(self):
        return "Feedback of "+self.name
