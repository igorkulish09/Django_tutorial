from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help_text = "Generates random users"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="Number of users to generate")

    def handle(self, *args, **options):
        count = options["count"]
        for _ in range(count):
            username = get_random_string(length=8)
            self.stdout.write(f"Created user with username: {username}")

        # users = []
        # for i in range(count):
        #     username = get_random_string()
        #     email = f"{username}@example.com"
        #     password = get_random_string()
        #     user = User(username=username, email=email)
        #     user.set_password(password)
        #     users.append(user)
        #
        # User.objects.bulk_create(users)
        #
        # self.stdout.write(self.style.SUCCESS(f"Successfully created {count} users"))
