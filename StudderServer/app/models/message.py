from django.db import models;

from app.models.user import User;
from app.models.match import Match;


class Message(models.Model):
    """description of class"""
    id = models.AutoField(primary_key = True);

    text = models.TextField(max_length = 1000);
    time = models.DateTimeField();
    readStatus = models.SmallIntegerField();

    match = models.ForeignKey(Match);
    sender = models.ForeignKey(User);

