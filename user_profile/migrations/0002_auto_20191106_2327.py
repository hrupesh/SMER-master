# Generated by Django 2.1.5 on 2019-11-06 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]