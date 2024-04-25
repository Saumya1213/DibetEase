from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

# class Cred(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     glucose_level = models.FloatField(null=True, blank=True)
#     height = models.FloatField(null=True, blank=True)
#     weight = models.FloatField(null=True, blank=True)
#     age = models.FloatField(null=True, blank=True)
#     timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     name = models.CharField(null=True, blank=True, max_length = 25)
    
#     def __str__(self):
#         if self.user:
#             return self.user.username  # Access username if user exists
#         else:
#             return "No associated user"
    
    

class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    age = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length = 25)
    
    def __str__(self):
        if self.user:
            return self.user.username  # Access username if user exists
        else:
            return "No associated user"
        

class HealthData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User model
    glucose_level = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            return self.user.username  # Access username if user exists