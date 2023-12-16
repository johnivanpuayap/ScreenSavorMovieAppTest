# Generated by Django 4.2.7 on 2023-12-16 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'unique_together': {('first_name', 'last_name')},
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'unique_together': {('first_name', 'last_name')},
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year_released', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(max_length=100)),
                ('cast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.cast')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
            options={
                'unique_together': {('movie', 'cast')},
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(through='movie.Role', to='movie.cast'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='movie.genre'),
        ),
    ]
