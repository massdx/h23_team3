from django.db import transaction
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from Account.models import Users
from BaseApi.AppEnum import UserRoleEnum
from Permission.models import Roles

class Seeder:
    @classmethod
    def seedUserRoles(cls):
        with transaction.atomic():
            for role in UserRoleEnum:
                user_role, created = Roles.objects.get_or_create(name=role.value, defaults={'description': role.value})
                if created:
                    user_role.save()

    @classmethod
    def seedPermissions(cls):
        with transaction.atomic():
            
            permission_customizes = [
                {
                    'codename': 'active_or_desactive_user',
                    'name': 'Active or Unactive user',
                    'type': Users,
                },
            ]

            for permission_data in permission_customizes:
                content_type = ContentType.objects.get_for_model(permission_data['type'])
                permission, _ = Permission.objects.update_or_create(
                    codename=permission_data['codename'],
                    content_type=content_type,
                    defaults={'name': permission_data['name']}
                )
                print(f"Permission '{permission.name}' created or updated.")


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding User types & Permissions...')
        Seeder.seedPermissions()
        Seeder.seedUserRoles()
        self.stdout.write(self.style.SUCCESS('Successfully seeded User types & permissions'))
