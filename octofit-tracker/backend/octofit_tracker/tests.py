from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        Activity.objects.create(user=ironman, type='Running', duration=30, date='2025-11-29')
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes.')
        Leaderboard.objects.create(team=marvel, points=120, rank=1)

    def test_user_count(self):
        self.assertEqual(User.objects.count(), 2)

    def test_team_count(self):
        self.assertEqual(Team.objects.count(), 2)

    def test_activity_count(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout_count(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard_count(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
