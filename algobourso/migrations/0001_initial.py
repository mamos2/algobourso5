# Generated by Django 2.0 on 2017-12-26 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LignePortefeuille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actions', models.CharField(choices=[('BNP', 'bnp'), ('TOTAL', 'total')], max_length=49)),
                ('date_ajout', models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")),
                ('date_achat', models.DateField()),
                ('date_vente', models.DateField()),
                ('prix_achat', models.FloatField()),
                ('prix_vente', models.FloatField()),
                ('prix_cloture', models.FloatField()),
                ('nbr_actions', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Portefeuille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portefeuille_name', models.CharField(max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StrategyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('nom', models.CharField(max_length=99)),
                ('url_script', models.TextField()),
                ('indicateurs_script', models.CharField(choices=[('RSI', 'rsi'), ('/data/indicators/macd.py', 'macd')], max_length=199)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('MAL', 'Homme'), ('FEM', 'Femme')], max_length=8)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ligneportefeuille',
            name='portefeuille',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algobourso.Portefeuille'),
        ),
    ]