# Generated by Django 3.1.2 on 2020-12-08 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20201208_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='maximo',
            field=models.CharField(default=1, max_length=56),
            preserve_default=False,
        ),
    ]