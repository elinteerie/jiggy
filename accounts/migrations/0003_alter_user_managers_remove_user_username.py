# Generated by Django 5.0.6 on 2024-06-04 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_institution_alter_user_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
