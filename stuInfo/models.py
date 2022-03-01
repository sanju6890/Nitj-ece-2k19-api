from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
