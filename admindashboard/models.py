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
