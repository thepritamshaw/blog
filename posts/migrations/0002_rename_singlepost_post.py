# Generated by Django 4.0 on 2024-03-14 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='singlePost',
            new_name='Post',
        ),
    ]
