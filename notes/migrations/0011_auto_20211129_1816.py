# Generated by Django 3.1.5 on 2021-11-29 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_auto_20211127_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='is_important',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
