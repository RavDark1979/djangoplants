# Generated by Django 2.2.28 on 2022-06-05 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magdziungla', '0016_auto_20220605_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='created',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='created',
            field=models.DateTimeField(blank=True),
        ),
    ]
