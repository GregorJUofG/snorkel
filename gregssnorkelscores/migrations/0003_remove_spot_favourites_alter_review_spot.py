# Generated by Django 4.2.11 on 2024-03-21 15:30

from django.db import migrations, models
import django.db.models.deletion
import gregssnorkelscores.models


class Migration(migrations.Migration):

    dependencies = [
        ('gregssnorkelscores', '0002_remove_spot_postcode_alter_location_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='favourites',
        ),
        migrations.AlterField(
            model_name='review',
            name='spot',
            field=models.ForeignKey(default=gregssnorkelscores.models.Review.get_default_spot, on_delete=django.db.models.deletion.CASCADE, to='gregssnorkelscores.spot'),
        ),
    ]
