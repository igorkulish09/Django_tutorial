from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help_del = "Deletes users"

    def add_arguments(self, parser):
        parser.add_argument("user_ids", nargs="+", type=int, help="User IDs to delete")

    def handle(self, *args, **options):
        user_ids = options["user_ids"]
        for user_id in user_ids:
            try:
                user = User.objects.get(id=user_id)
                if user.is_superuser:
                    raise ValueError("Cannot delete superuser")
                user.delete()
                self.stdout.write(f"Deleted user with ID: {user_id}")
            except User.DoesNotExist:
                self.stdout.write(f"User with ID {user_id} does not exist")
            except ValueError as e:
                self.stdout.write(str(e))
