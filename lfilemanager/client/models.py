from django.db import models



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    last_login = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "users"

class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)    
    
    def __str__(self):
        return self.name

    last_login = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "users"

# Create your models here.
