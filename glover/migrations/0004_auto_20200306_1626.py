# Generated by Django 2.2.4 on 2020-03-06 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glover', '0003_auto_20200305_2222'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('profile', 'profile_liked')},
        ),
    ]