# Generated by Django 2.0 on 2018-01-01 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algobourso', '0013_auto_20171228_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strategyuser',
            name='actions',
        ),
        migrations.AddField(
            model_name='strategyuser',
            name='actions',
            field=models.CharField(blank=True, choices=[('/data/apple.csv', 'apple'), ('TOTAL', 'total')], max_length=49, null=True),
        ),
        migrations.DeleteModel(
            name='ActionData',
        ),
    ]
