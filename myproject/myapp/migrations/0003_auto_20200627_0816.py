# Generated by Django 3.0.6 on 2020-06-27 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200627_0746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friends',
            old_name='Organization',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='friends',
            old_name='profission',
            new_name='profession',
        ),
        migrations.AlterField(
            model_name='friends',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
