# Generated by Django 4.2.5 on 2023-10-25 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0008_remove_room_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_type',
        ),
    ]