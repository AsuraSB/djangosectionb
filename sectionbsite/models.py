from django.db import models

class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True)
    gender = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'genders'
        
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55, blank=True)
    last_name = models.CharField(max_length=55)
    age = models.IntegerField()
    birth_date = models.DateField()
    gender = models.ForeignKey()
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'