# Generated by Django 4.0.4 on 2022-05-05 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_commande_type_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='ligne_huit',
            field=models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Ligne 8'),
        ),
        migrations.AddField(
            model_name='commande',
            name='ligne_huit_prix_total',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='Ligne Total (D)'),
        ),
        migrations.AddField(
            model_name='commande',
            name='ligne_huit_prix_unitaire',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='Prix Unitaire (D)'),
        ),
        migrations.AddField(
            model_name='commande',
            name='ligne_huit_qte',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='Quantite'),
        ),
        migrations.AddField(
            model_name='commande',
            name='ligne_sept',
            field=models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Ligne 7'),
        ),
        migrations.AddField(
            model_name='commande',
            name='ligne_sept_prix_total',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='Ligne Total (D)'),
        ),
        migrations.AddField(
            model_name='commande',
            name='ligne_sept_prix_unitaire',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='Prix Unitaire (D)'),
        ),
        migrations.AddField(
            model_name='commande',
            name='ligne_sept_qte',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='Quantite'),
        ),
        migrations.AddField(
            model_name='commande',
            name='ligne_six',
            field=models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Ligne 6'),
        ),
        migrations.AddField(
            model_name='commande',
            name='ligne_six_prix_total',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='Ligne Total (D)'),
        ),
        migrations.AddField(
            model_name='commande',
            name='ligne_six_prix_unitaire',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='Prix Unitaire (D)'),
        ),
        migrations.AddField(
            model_name='commande',
            name='ligne_six_qte',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='Quantite'),
        ),
    ]
