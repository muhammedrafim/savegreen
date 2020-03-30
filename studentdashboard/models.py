from django.db import models
from admindashboard.models import ClassSection,Class,Subject
from teacherdashboard.models import teachers
# Create your models here.

class parent(models.Model):
    father_name = models.TextField(max_length=20)
    mothers_name = models.TextField(max_length=20)
    occupation = models.TextField()
    contact_info = models.DecimalField(max_digits=15,decimal_places=0)
    alternate_contact_info = models.DecimalField(max_digits=15,decimal_places=0)
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
    phone_number = models.DecimalField(max_digits=12,decimal_places=0)
    image = models.ImageField(upload_to='students')
    registration_id = models.TextField()
    class_name = models.TextField()
    class_division = models.TextField()
    roll_number = models.IntegerField()
    last_school = models.TextField()
    last_std = models.TextField()
    last_marks_obtained = models.TextField()
    sports_intreseted = models.TextField()
    attendence_blocked = models.TextField()
    parent = models.ForeignKey(parent,on_delete=models.CASCADE)

class attendance(models.Model):
    student = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    class_details = models.ForeignKey(Class,on_delete=models.DO_NOTHING)
    section = models.ForeignKey(ClassSection,on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    is_present = models.BooleanField()
    remarks = models.TextField()
    teacher_id = models.ForeignKey(teachers,on_delete=models.DO_NOTHING)
    date_marked = models.DateField()