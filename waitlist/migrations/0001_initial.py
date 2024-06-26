# Generated by Django 5.0.6 on 2024-05-30 08:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('expected_graduation_year', models.IntegerField()),
                ('JIggy_coin_balance', models.IntegerField(default=0)),
                ('referral_code', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=290)),
                ('short_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referred_bonus', models.IntegerField(default=50)),
                ('referred_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referred_by', to='waitlist.student')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrals', to='waitlist.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='university_or_college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='university_of_student', to='waitlist.university'),
        ),
    ]
