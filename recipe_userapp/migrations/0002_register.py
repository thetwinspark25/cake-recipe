# Generated by Django 4.1.6 on 2023-02-27 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
