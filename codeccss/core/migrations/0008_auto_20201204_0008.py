# Generated by Django 3.1.2 on 2020-12-04 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201203_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='modulo',
        ),
        migrations.AddField(
            model_name='perfil',
            name='modulo',
            field=models.ManyToManyField(blank=True, null=True, to='core.Modulo'),
        ),
    ]