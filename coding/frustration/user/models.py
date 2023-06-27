from django.db import models

# Create your models here.
class RegistrationModel(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    userid = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=100)
    emailid = models.EmailField(max_length=100)
    gender = models.CharField(max_length=100)
class AnswerModel(models.Model):
    userId = models.ForeignKey(RegistrationModel,on_delete = models.CASCADE)
    sessionone = models.IntegerField(default=0)
    sessiontwo = models.IntegerField(default=0)
    sessionthree = models.IntegerField(default=0)
    sessionfour = models.IntegerField(default=0)
    sessionfive = models.IntegerField(default=0)
    catagory = models.CharField(max_length=100)

class FeedbackModel(models.Model):
    username = models.ForeignKey(RegistrationModel,on_delete = models.CASCADE)
    feedback = models.CharField(max_length=300)