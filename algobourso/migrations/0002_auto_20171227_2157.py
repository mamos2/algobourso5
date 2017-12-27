# Generated by Django 2.0 on 2017-12-27 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('algobourso', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indicateurs',
            old_name='strategyUser',
            new_name='strategyuser',
        ),
        migrations.RemoveField(
            model_name='sma',
            name='strategyUser',
        ),
        migrations.AddField(
            model_name='sma',
            name='strategyuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='algobourso.StrategyUser'),
        ),
        migrations.AlterField(
            model_name='sma',
            name='indicateurs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='algobourso.Indicateurs'),
        ),
    ]