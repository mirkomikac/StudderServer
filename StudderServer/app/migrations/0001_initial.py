# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-19 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=1000)),
                ('time', models.DateTimeField()),
                ('readStatus', models.SmallIntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Match')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=40, null=True)),
                ('birthday', models.DateField()),
                ('onlineStatus', models.NullBooleanField()),
                ('lastOnline', models.DateTimeField(null=True)),
                ('radius', models.FloatField(null=True)),
                ('latitude', models.CharField(max_length=20, null=True)),
                ('longtitude', models.CharField(max_length=20, null=True)),
                ('profileCreated', models.DateField(null=True)),
                ('shareLocation', models.NullBooleanField()),
                ('sex', models.SmallIntegerField()),
                ('interestedIn', models.SmallIntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='match',
            name='firstParticipate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='firstParticipate', to='app.User'),
        ),
        migrations.AddField(
            model_name='match',
            name='secondParticipate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondParticipate', to='app.User'),
        ),
    ]
