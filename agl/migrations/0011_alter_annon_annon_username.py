# Generated by Django 5.0.6 on 2024-07-30 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agl', '0010_remove_annon_pass_code_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annon',
            name='annon_username',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]