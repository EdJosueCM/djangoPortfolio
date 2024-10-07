from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField
import datetime


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    hours = models.CharField(max_length=20)
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['name','date']
        
    def __str__(self):
        return f"{self.name}"