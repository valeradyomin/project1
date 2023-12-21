from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='su@sky.pro',
            first_name='admin',
            last_name='root',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('111')
        user.save()