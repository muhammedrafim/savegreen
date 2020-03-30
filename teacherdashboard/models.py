from django.db import models
#from admindashboard.models import ClassSection,Class,Subject
# Create your models here.
class teachers(models.Model):
    firstname = models.TextField(max_length=15)
    middlename = models.TextField(max_length=15)
    lastname = models.TextField(max_length=15)
    gender = models.TextField()
    dateofbirth = models.DateField()
    email = models.EmailField()
    religion = models.TextField()
    phone_number = models.DecimalField(max_digits=12,decimal_places=0)
    image = models.ImageField(upload_to='teachers')
    address = models.TextField()
    address_alternate = models.TextField()
    country = models.TextField()
    state = models.TextField()
    pincode = models.IntegerField()
    alternate_phone = models.DecimalField(max_digits=12,decimal_places=0)
    highest_degree = models.TextField()
    highest_degree_university = models.TextField()
    highest_degree_yearpassed = models.TextField()
    highest_degree_cgpa = models.TextField()
    degree = models.TextField()
    university = models.TextField()
    yearpassed = models.TextField()
    cgpa = models.TextField()
    username = models.TextField()


