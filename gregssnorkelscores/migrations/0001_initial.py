# Generated by Django 2.2.28 on 2024-03-22 16:09

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
                ('about', models.CharField(default='Default text :)', max_length=500)),
                ('reviewsAmount', models.IntegerField(default=0)),
                ('reviewsAverage', models.FloatField(default=0)),
                ('slug', models.SlugField(unique=True)),
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
                ('reviewsAmount', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('favourites', models.ManyToManyField(blank=True, default=None, related_name='favourites', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(default=gregssnorkelscores.models.Spot.get_default_location, on_delete=django.db.models.deletion.CASCADE, to='gregssnorkelscores.Location')),
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
                ('comment', models.TextField(max_length=500)),
                ('rating', models.IntegerField(choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')], default=1)),
                ('likes', models.IntegerField(default=0)),
                ('spot', models.ForeignKey(default=gregssnorkelscores.models.Review.get_default_spot, on_delete=django.db.models.deletion.CASCADE, to='gregssnorkelscores.Spot')),
            ],
            options={
                'verbose_name': 'Spot Review',
                'verbose_name_plural': 'Spot Reviews',
            },
        ),
    ]
