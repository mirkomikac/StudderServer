from django.db import models;

class User(models.Model):
    """description of class"""
    id = models.AutoField(primary_key = True);

    name = models.CharField(max_length = 40, null = False);
    surname = models.CharField(max_length = 40, null = False);
    description = models.TextField(max_length = 40, null = True);
    birthday = models.DateField(null = False);
    onlineStatus = models.NullBooleanField(null = True);
    lastOnline = models.DateTimeField(null = True);
    radius = models.FloatField(null = True);
    latitude = models.CharField(max_length = 20, null = True);
    longtitude = models.CharField(max_length = 20, null = True);
    profileCreated = models.DateField(null = True);
    shareLocation = models.NullBooleanField(null = True);
    sex = models.SmallIntegerField(null = False);
    interestedIn = models.SmallIntegerField(null = True);


 



