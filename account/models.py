from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Profile(models.Model):
    # foreign key for table profile
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # new columns
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    birthday = models.DateField()
    
    def __str__(self):
        return self.User.username
    
