from django.db import models
from admindashboard.models import ClassSection,Class,Subject
from teacherdashboard.models import teachers
from django.contrib.auth.models import User
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
    class_name = models.ForeignKey(Class,on_delete=models.CASCADE)
    class_division = models.ForeignKey(ClassSection,on_delete=models.CASCADE)
    roll_number = models.IntegerField()
    last_school = models.TextField()
    last_std = models.TextField()
    last_marks_obtained = models.TextField()
    sports_intreseted = models.TextField()
    attendence_blocked = models.TextField(default='No')
    login_details = models.ForeignKey(User,on_delete=models.CASCADE)
    parent = models.ForeignKey(parent,on_delete=models.CASCADE)

class attendance(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    class_details = models.ForeignKey(Class,on_delete=models.CASCADE)
    section = models.ForeignKey(ClassSection,on_delete=models.CASCADE)
    is_present = models.BooleanField()
    remarks = models.TextField()
    teacher_id = models.ForeignKey(teachers,on_delete=models.CASCADE)
    date_marked = models.DateField()

class marks(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class,on_delete=models.CASCADE)
    section = models.ForeignKey(ClassSection,on_delete=models.CASCADE)
    exam_type = models.TextField()
    marks_obtained = models.TextField()
    total_marks = models.TextField()
    remarks = models.TextField()
    marked_by = models.ForeignKey(teachers,on_delete=models.CASCADE)
