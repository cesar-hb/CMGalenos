# Generated by Django 4.2.7 on 2023-11-20 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmg', '0002_remove_atencionmedica_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencionmedica',
            name='fecha',
            field=models.DateField(verbose_name='Fecha atención'),
        ),
    ]
