# Generated by Django 5.0.2 on 2024-04-03 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_travel_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('pimage', models.ImageField(upload_to='images/')),
                ('pckname', models.CharField(max_length=50)),
                ('pcountry', models.CharField(max_length=50)),
                ('pplace', models.CharField(max_length=50)),
                ('pdays', models.IntegerField()),
                ('prate', models.IntegerField()),
            ],
        ),
    ]
