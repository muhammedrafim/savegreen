from django.db import models

# Create your models here.
class Announcement(models.Model):
    type = models.TextField()
    announced_for = models.TextField()
    subject = models.TextField()
    description = models.TextField()

class Class(models.Model):
    class_name = models.TextField()
    class_code = models.TextField()
    class_teacher = models.TextField()
    description = models.TextField()

class ClassSection(models.Model):
    class_name = models.TextField()
    section_name = models.TextField()
    section_code = models.TextField()
    description = models.TextField()

class Subject(models.Model):
    name = models.TextField()
    code = models.TextField()
    teacher = models.TextField()
    subject_class = models.TextField()
    description = models.TextField()
