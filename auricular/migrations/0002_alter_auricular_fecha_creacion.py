# Generated by Django 4.2.6 on 2023-11-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auricular', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auricular',
            name='fecha_creacion',
            field=models.IntegerField(),
        ),
    ]
