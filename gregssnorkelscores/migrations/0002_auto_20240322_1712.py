# Generated by Django 2.2.28 on 2024-03-22 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gregssnorkelscores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.CharField(max_length=128),
        ),
    ]
