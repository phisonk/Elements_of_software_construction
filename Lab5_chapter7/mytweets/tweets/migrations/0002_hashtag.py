# Generated by Django 2.1 on 2018-08-29 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('tweet', models.ManyToManyField(to='tweets.Tweet')),
            ],
        ),
    ]