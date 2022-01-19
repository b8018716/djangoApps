from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    submission_date = models.DateTimeField()
    description = models.TextField(blank=True)
    authors = models.ManyToManyField('author',blank=True)

class Author(models.Model):
    Gender_Choices=[('F', 'Female'),('M', 'Male'),('Other','Other')]
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=Gender_Choices,blank=True)
    dob = models.DateField()


# Create your models here.
