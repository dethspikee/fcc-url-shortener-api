# Generated by Django 3.0.5 on 2020-04-21 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200421_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='original_url',
            field=models.CharField(max_length=200),
        ),
    ]
