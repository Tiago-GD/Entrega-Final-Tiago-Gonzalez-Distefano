# Generated by Django 4.2.6 on 2023-11-18 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0005_alter_datosextra_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosextra',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
