# Generated by Django 4.0.4 on 2022-05-04 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='type_commande',
            field=models.CharField(blank=True, choices=[('Reception', 'Reception'), ('Commande', 'Commande')], default='', max_length=50, null=True),
        ),
    ]
