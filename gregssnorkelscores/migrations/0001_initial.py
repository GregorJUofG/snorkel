# Generated by Django 2.2.28 on 2024-03-13 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('picture', models.ImageField(blank=True, upload_to='location_images')),
                ('about', models.CharField(max_length=500)),
                ('favourites', models.IntegerField()),
                ('reviewsAmount', models.IntegerField()),
                ('reviewsAverage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
            ],
        ),
        migrations.CreateModel(
            name='Spots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('url', models.URLField()),
                ('picture', models.ImageField(blank=True, upload_to='spot_images')),
                ('postcode', models.CharField(max_length=8)),
                ('reviewsAmount', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gregssnorkelscores.Location')),
            ],
        ),
    ]
