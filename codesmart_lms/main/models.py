from django.db import models

# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254,blank=True, null=True)
    password = models.CharField(max_length=200)
    qualifications = models.CharField(max_length=200,blank=True, null=True)
    mobile_number = models.CharField(max_length=200, blank=True, null=True)
    address =  models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name

class CourseCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'course categories'

class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='course_categories')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teachers')
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254,blank=True, null=True)
    password = models.CharField(max_length=200)
    qualifications = models.CharField(max_length=200,blank=True, null=True)
    mobile_number = models.CharField(max_length=200, blank=True, null=True)
    address =  models.TextField(blank=True, null=True)
    Intrested_categories = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='intrested_categories') 

    def __str__(self):
        return self.full_name

