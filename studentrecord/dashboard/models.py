from django.db import models
import random


classifications = [
    ('FR', 'Freshman'),
    ('SP', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior')
]

majors = [
    ('CS', 'Computer Science'),
    ('BIO', 'Biology')
]


# Create your models here.

#user ==> student (login)
#student (fname, lname, age, school email, courses, gpa, advisor, )
#course
#advisor

class Department(models.Model):
    name = models.CharField(max_length=250, null=True, blank=False)

    def __str__(self):
        return self.name

class Advisor(models.Model):
    department = models.ForeignKey("Department", on_delete=models.SET_NULL, null=True, blank=False)
    first_name = models.CharField(max_length=250, null=True, blank=False)
    last_name = models.CharField(max_length=250, null=True, blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Student(models.Model):
    advisor = models.ForeignKey('Advisor', on_delete=models.SET_NULL, null=True, blank=False)
    department = models.ForeignKey("Department", on_delete=models.SET_NULL, null=True, blank=False)
    first_name = models.CharField(max_length=250, null=True, blank=False)
    last_name = models.CharField(max_length=250, null=True, blank=False)
    age = models.PositiveIntegerField(default=18, null=True, blank=False)
    email = models.EmailField(max_length=254, null=True, blank=False)
    classification = models.CharField(max_length=250, null=True, blank=False, choices=classifications)
    major = models.CharField(max_length=250, null=True, blank=False, choices=majors)
    courses = models.ManyToManyField('Course')
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def gen_id(self):
        prefix = "%s%s" %(self.classification, ord(self.classification[0])+ord(self.classification[1]))
        count = 1
        while 1:
            student_id = "%s%s" %(prefix, count)
            if not Student.objects.get(id=student_id):
                self.id = student_id
                self.save()
                break
            count += 1
    
    def __str__(self):
        return self.first_name + " " + self.last_name


class Course(models.Model):
    department = models.ForeignKey("Department", on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=250, null=True, blank=False)
    credit_hours = models.IntegerField(default=3)

    def __str__(self):
        return self.name