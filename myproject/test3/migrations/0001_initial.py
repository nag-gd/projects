# Generated by Django 3.0.6 on 2020-07-11 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('contactinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='test3.Contactinfo')),
                ('grade', models.IntegerField(null=True)),
            ],
            bases=('test3.contactinfo',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('contactinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='test3.Contactinfo')),
                ('Experience', models.IntegerField(null=True)),
            ],
            bases=('test3.contactinfo',),
        ),
    ]
