# Generated by Django 5.0.6 on 2024-05-30 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='JIggy_coin_balance',
            new_name='jiggy_coin_balance',
        ),
    ]
