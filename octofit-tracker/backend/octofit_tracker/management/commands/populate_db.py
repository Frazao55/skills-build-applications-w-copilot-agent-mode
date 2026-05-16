from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='captain@marvel.com', name='Captain America', team='marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='superman@dc.com', name='Superman', team='dc'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc'),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user='ironman@marvel.com', activity_type='run', duration=30, date='2024-01-01'),
            Activity(user='captain@marvel.com', activity_type='cycle', duration=45, date='2024-01-02'),
            Activity(user='spiderman@marvel.com', activity_type='swim', duration=25, date='2024-01-03'),
            Activity(user='batman@dc.com', activity_type='run', duration=40, date='2024-01-01'),
            Activity(user='superman@dc.com', activity_type='cycle', duration=60, date='2024-01-02'),
            Activity(user='wonderwoman@dc.com', activity_type='swim', duration=35, date='2024-01-03'),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        leaderboard = [
            Leaderboard(user='ironman@marvel.com', points=120, rank=1),
            Leaderboard(user='superman@dc.com', points=110, rank=2),
            Leaderboard(user='captain@marvel.com', points=100, rank=3),
            Leaderboard(user='batman@dc.com', points=90, rank=4),
            Leaderboard(user='spiderman@marvel.com', points=80, rank=5),
            Leaderboard(user='wonderwoman@dc.com', points=70, rank=6),
        ]
        for lb in leaderboard:
            lb.save()

        # Workouts
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups', difficulty='easy'),
            Workout(name='Situps', description='Do 30 situps', difficulty='easy'),
            Workout(name='Squats', description='Do 40 squats', difficulty='medium'),
            Workout(name='Plank', description='Hold plank for 2 minutes', difficulty='hard'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
