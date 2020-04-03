from django.db import models
from teacherdashboard.models import teachers
# Create your models here.
class Announcement(models.Model):
    type = models.TextField()
    announced_for = models.TextField()
    subject = models.TextField()
    description = models.TextField()

class Class(models.Model):
    class_name = models.TextField()
    class_code = models.TextField()
    description = models.TextField()

class ClassSection(models.Model):
    class_name = models.ForeignKey(Class,on_delete=models.CASCADE)
    section_teacher = models.ForeignKey(teachers,on_delete=models.DO_NOTHING)
    section_name = models.TextField()
    section_code = models.TextField()
    description = models.TextField()

class Subject(models.Model):
    name = models.TextField()
    code = models.TextField()
    teacher = models.ForeignKey(teachers,on_delete=models.CASCADE)
    subject_class = models.ForeignKey(Class,on_delete=models.CASCADE)
    subject_section = models.ForeignKey(ClassSection,on_delete=models.CASCADE)
    description = models.TextField()

class TimeTable(models.Model):
    day = models.TextField()
    time_slot = models.TextField()
    class_name = models.TextField()
    class_section = models.TextField()
    subject_name = models.TextField()
    teacher = models.TextField()
    classroom = models.TextField()

