from django.db import models

# Create your models here.
class StudentModel(models.Model):
    stname = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)

class Post(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField()

class col(models.Model):
    colorname = models.CharField(max_length=100)
    cname = models.CharField(max_length=20, blank=True, null=True)
    cplusname = models.CharField(max_length=20, blank=True, null=True)
    javaname = models.CharField(max_length=20, blank=True, null=True)
    pythonname = models.CharField(max_length=20, blank=True, null=True)

class chkboxinsert(models.Model):
    coursename = models.CharField(max_length=100)

class Player(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    title = models.TextField(max_length=65)
    price = models.FloatField(default=0)
    withEndDate = models.BooleanField(default=False)
    endDate = models.DateField(blank=True,null=True)
    description = models.CharField(max_length=65, default='asd', null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

class col3(models.Model):
    cname = models.CharField(max_length=20, blank=True, null=True)
    cplusname = models.CharField(max_length=20, blank=True, null=True)
    javaname = models.CharField(max_length=20, blank=True, null=True)
    pythonname = models.CharField(max_length=20, blank=True, null=True)
