# Generated by Django 4.2.5 on 2023-09-29 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='titles',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
