# Generated by Django 5.0.6 on 2024-07-30 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agl', '0004_anonchat'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonchat',
            name='group',
            field=models.BooleanField(default=False),
        ),
    ]
