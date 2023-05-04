from django.db import models

# Create your models here.

class Teams(models.Model):
    teamname = models.CharField(max_length=30)
    team_color = models.CharField(max_length=30, primary_key=True)
    
class Courses(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course = models.CharField(max_length=30)
    
class Students(models.Model):
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.BooleanField()
    course = models.ForeignKey(
        "Courses" , on_delete=models.CASCADE)
    teams = models.ForeignKey(
        "Teams" , on_delete=models.CASCADE)
    
    