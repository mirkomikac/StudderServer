from django.db import models;

from app.models.user import User;

class Match(models.Model):
    """description of class"""
    id = models.AutoField(primary_key = True);

    firstParticipate = models.ForeignKey(User, related_name='firstParticipate');
    secondParticipate = models.ForeignKey(User, related_name='secondParticipate');

