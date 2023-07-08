from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help_text = "Generates random users"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="Indicates the number of users to be created")

    def handle(self, *args, **kwargs):
        count = kwargs["count"]

        if count < 1 or count > 10:
            raise ValueError("Count should be between 1 and 10")

        users = []
        for i in range(count):
            username = get_random_string(length=10)
            email = f"{username}@example.com"
            password = get_random_string(length=10)
            user = User(username=username, email=email)
            user.set_password(password)
            users.append(user)

        User.objects.bulk_create(users)

        self.stdout.write(self.style.SUCCESS(f"Successfully created {count} users"))
