# Generated by Django 5.0.6 on 2024-07-30 21:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agl', '0007_remove_anonchat_message_anonchat_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annon',
            old_name='Annon_username',
            new_name='annon_username',
        ),
        migrations.RemoveField(
            model_name='annon',
            name='group',
        ),
        migrations.RemoveField(
            model_name='annon',
            name='pass_code',
        ),
        migrations.AddField(
            model_name='anonchat',
            name='annon_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agl.annon'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anonchat',
            name='group',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='anonchat',
            name='pass_code',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]