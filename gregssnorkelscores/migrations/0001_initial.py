# Generated by Django 4.2.11 on 2024-03-21 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gregssnorkelscores.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('pictures', models.ImageField(blank=True, upload_to='location_images')),
                ('about', models.CharField(default=None, max_length=500)),
                ('reviewsAmount', models.IntegerField(default=0)),
                ('reviewsAverage', models.FloatField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Publication Date')),
            ],
            options={
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('pictures', models.ImageField(blank=True, upload_to='profile_images')),
                ('experience', models.CharField(max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('author', models.CharField(max_length=128)),
                ('pictures', models.ImageField(blank=True, upload_to='spot_images')),
                ('postcode', models.CharField(max_length=8)),
                ('reviewsAmount', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Publication Date')),
                ('slug', models.SlugField(unique=True)),
                ('favourites', models.ManyToManyField(blank=True, default=None, related_name='favourites', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(default=gregssnorkelscores.models.Spot.get_default_location, on_delete=django.db.models.deletion.CASCADE, to='gregssnorkelscores.location')),
            ],
            options={
                'verbose_name_plural': 'Spots',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=128)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Publication Date')),
                ('comment', models.TextField(max_length=500)),
                ('rating', models.IntegerField(choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')], default=1)),
                ('likes', models.IntegerField(default=0)),
                ('spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gregssnorkelscores.spot')),
            ],
            options={
                'verbose_name': 'Spot Review',
                'verbose_name_plural': 'Spot Reviews',
                'ordering': ['-pub_date'],
            },
        ),
    ]
