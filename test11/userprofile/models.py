from django.db import models

# Create your models here.
class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class FamilyMember(models.Model):
    name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)