# Generated by Django 4.2.5 on 2023-10-25 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0005_alter_feedback_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='status',
            field=models.CharField(default='not approved', max_length=20),
        ),
    ]