from django.db import models
from djongo import models as djongo_models

class Team(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)

class User(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = djongo_models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

class Activity(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    user = djongo_models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # minutes
    date = models.DateField()

class Workout(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = djongo_models.ManyToManyField(Team, related_name='workouts')

class Leaderboard(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    team = djongo_models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
    points = models.IntegerField()
    rank = models.IntegerField()
