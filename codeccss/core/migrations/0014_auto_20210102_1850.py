# Generated by Django 3.1.2 on 2021-01-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_historial_redaccion_modulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial_redaccion',
            name='valor',
            field=models.IntegerField(),
        ),
    ]
