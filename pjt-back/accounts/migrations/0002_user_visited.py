# Generated by Django 3.2.13 on 2022-11-21 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='visited',
            field=models.ManyToManyField(related_name='visited_movie', to='movies.Movie'),
        ),
    ]
