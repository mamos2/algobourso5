# Generated by Django 2.0 on 2017-12-28 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algobourso', '0004_auto_20171228_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sma',
            name='indicateurs',
        ),
        migrations.AddField(
            model_name='indicateurs',
            name='sma',
            field=models.ManyToManyField(blank=True, to='algobourso.sma'),
        ),
    ]
