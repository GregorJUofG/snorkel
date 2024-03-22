# Generated by Django 2.2.28 on 2024-03-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gregssnorkelscores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='slug',
            field=models.SlugField(default='default', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spot',
            name='slug',
            field=models.SlugField(default='default', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='favourites',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='location',
            name='reviewsAmount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='location',
            name='reviewsAverage',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='spot',
            name='reviewsAmount',
            field=models.IntegerField(default=0),
        ),
    ]