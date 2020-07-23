# Generated by Django 3.0.6 on 2020-07-05 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('author', models.CharField(max_length=35)),
                ('price', models.FloatField()),
            ],
        ),
    ]
