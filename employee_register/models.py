from django.db import models

class Position(models.Model):
     position = models.CharField(max_length=50)
     def __str__(self):
          return self.position
     

class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    emp_code = models.CharField(max_length=3)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    

    def __str__(self):
          return self.firstname
     
