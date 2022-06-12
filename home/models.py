from django.db import models
from django.forms import modelformset_factory

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=122)
    lastname =models.CharField(max_length=122)    
    email =models.EmailField(max_length=122)
    books = models.TextField()
    gender = models.CharField(max_length=10)
    schools = models.TextField()

class School(models.Model):
    school = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    principal = models.CharField(max_length=122)
    phone =models.CharField(max_length=122)
    address2 =models.TextField(max_length=122)
    
class Book(models.Model):
    title = models.CharField(max_length=122)
    author_name =models.CharField(max_length=122) 
    date_of_Publication = models.CharField(max_length=122)
    number_of_Pages = models.CharField(max_length=122)

    

    