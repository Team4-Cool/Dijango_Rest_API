from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin_field = models.CharField(max_length=100)

    def __str__(self):
        return self.user