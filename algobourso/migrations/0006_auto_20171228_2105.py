# Generated by Django 2.0 on 2017-12-28 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('algobourso', '0005_auto_20171228_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicateurs',
            name='sma',
        ),
        migrations.AddField(
            model_name='sma',
            name='indicateurs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='algobourso.Indicateurs'),
        ),
    ]