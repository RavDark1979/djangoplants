# Generated by Django 2.2.28 on 2022-06-05 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magdziungla', '0014_auto_20220605_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='created',
            field=models.DateTimeField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='plant',
            field=models.ManyToManyField(blank=True, to='magdziungla.Plant'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='pot',
            field=models.ManyToManyField(blank=True, to='magdziungla.Pot'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='soil',
            field=models.ManyToManyField(blank=True, to='magdziungla.Soil'),
        ),
    ]
