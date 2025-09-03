
from django.db import migrations


def create_roles(apps, schema_editor):
    RoleModel = apps.get_model("security", "RoleModel")
    system_roles = ['doctor', 'nurse', 'staff', 'volunteer', 'administrator']

    for role_name in system_roles:
        role, created = RoleModel.objects.get_or_create(
            name=role_name,
            defaults={"description": "", "is_system": True}
        )
        if not created:
            # Ensure consistency if already exists
            RoleModel.objects.filter(pk=role.pk).update(is_system=True)


def delete_roles(apps, schema_editor):
    RoleModel = apps.get_model("security", "RoleModel")
    RoleModel.objects.filter(
        name__in=['doctor', 'nurse', 'staff', 'volunteer', 'administrator'],
        is_system=True
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0003_migrate_default_role_change'),
    ]

    operations = [
        migrations.RunPython(create_roles, delete_roles),
    ]
