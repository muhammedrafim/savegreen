from django.db import models

# Create your models here.

class parent(models.Model):
    father_name = models.TextField(max_length=20)
    mothers_name = models.TextField(max_length=20)
    occupation = models.TextField()
    contact_info = models.IntegerField()
    alternate_contact_info = models.IntegerField()
    email = models.EmailField()
    religion = models.TextField()
    nationality = models.TextField()
    address = models.TextField()
    country = models.TextField()
    state = models.TextField()
    pincode = models.IntegerField()
    image = models.ImageField(upload_to='students')



class Student(models.Model):
    firstname = models.TextField(max_length=15)
    middlename = models.TextField(max_length=15)
    lastname = models.TextField(max_length=15)
    gender = models.TextField()
    dateofbirth = models.DateField()
    email = models.EmailField()
    religion = models.TextField()
    phone_number = models.IntegerField()
    image = models.ImageField(upload_to='students')
    registration_id = models.TextField()
    class_name = models.TextField()
    class_division = models.TextField()
    roll_number = models.IntegerField()
    last_school = models.TextField()
    last_std = models.TextField()
    last_marks_obtained = models.DecimalField(max_digits=8,decimal_places=2)
    sports_intreseted = models.TextField()
    parent = models.ForeignKey(parent,on_delete=models.CASCADE)

