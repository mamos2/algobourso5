# Generated by Django 2.0 on 2017-12-27 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algobourso', '0003_auto_20171227_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sma',
            name='strategyuser',
        ),
        migrations.RemoveField(
            model_name='indicateurs',
            name='strategyuser',
        ),
        migrations.AddField(
            model_name='indicateurs',
            name='strategyuser',
            field=models.ManyToManyField(to='algobourso.StrategyUser'),
        ),
    ]