# Generated by Django 3.2.3 on 2021-06-01 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AEROLINEA', '0004_aeropuerto_vuelo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vuelo',
            name='destino',
        ),
        migrations.RemoveField(
            model_name='vuelo',
            name='origen',
        ),
        migrations.DeleteModel(
            name='Aeropuerto',
        ),
        migrations.DeleteModel(
            name='Vuelo',
        ),
    ]
