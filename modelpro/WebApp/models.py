from django.db import models

# Create your models here.clas
class Employee(models.Model):
    #Id=models.AutoField()
    Name=models.CharField(max_length=100)
    Age=models.IntegerField(default=18)
    Email=models.EmailField(max_length=100)
    Address=models.TextField(null=True,blank=True)
    Image=models.ImageField()
    File=models.FileField()

class Car(models.Model):
    Car_name=models.CharField(max_length=100)
    Speed=models.IntegerField(default=50)

    def __str__(self):
        return self.Car_name
    

