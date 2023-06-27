from django.db import models

# Create your models here.
class NotificationModel(models.Model):
    date = models.DateField()
    notifications = models.CharField(max_length=300)