# Generated by Django 5.1.3 on 2024-11-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=128, verbose_name='Street name')),
                ('city', models.ManyToManyField(to='countries.city')),
            ],
        ),
    ]
