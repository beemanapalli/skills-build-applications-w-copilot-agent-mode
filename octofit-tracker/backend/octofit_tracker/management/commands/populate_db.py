from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        for obj in Activity.objects.all():
            if obj.pk:
                obj.delete()
        for obj in Workout.objects.all():
            if obj.pk:
                obj.delete()
        for obj in Leaderboard.objects.all():
            if obj.pk:
                obj.delete()
        for obj in User.objects.all():
            if obj.pk:
                obj.delete()
        for obj in Team.objects.all():
            if obj.pk:
                obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Running', duration=25, date=timezone.now().date())
        Activity.objects.create(user=users[4], type='Cycling', duration=50, date=timezone.now().date())
        Activity.objects.create(user=users[5], type='Swimming', duration=40, date=timezone.now().date())

        # Create workouts
        w1 = Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes.')
        w2 = Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility.')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([dc])

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=120, rank=1)
        Leaderboard.objects.create(team=dc, points=110, rank=2)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
