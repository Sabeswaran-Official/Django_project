
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    age = models.IntegerField(default=0 )
    role=models.CharField(max_length=50,null=True)
    ph_no=models.IntegerField(null=True)

    def __str__(self):
        return self.username 
