# Generated by Django 4.2.3 on 2023-09-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='typee',
            field=models.CharField(choices=[('Berline', 'berline'), ('Coupée', 'Coupée'), ('Hayon', 'Hayon'), ('Pick-up', 'Pick-up'), ('Crossover', 'Crossover'), ('SUV', 'SUV'), ('Fourgonettes', 'Fourgonettes'), ('Cabriolets', 'Cabriolets'), ('Roadsters', 'Roadsters'), ('Targa', 'Targa'), ('citadine', 'citadine')], max_length=20),
        ),
    ]