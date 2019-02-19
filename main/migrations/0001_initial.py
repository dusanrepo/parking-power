# Generated by Django 2.1.7 on 2019-02-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authorization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=50)),
                ('vehicle_name', models.CharField(max_length=50)),
                ('make_model', models.CharField(max_length=50)),
                ('vehicle_color', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=50)),
                ('is_authorized', models.IntegerField()),
            ],
        ),
    ]
