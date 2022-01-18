from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    submission_date = models.DateTimeField()
    description = models.TextField(blank=True)




# Create your models here.
