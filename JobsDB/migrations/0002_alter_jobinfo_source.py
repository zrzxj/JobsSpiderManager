# Generated by Django 3.2.4 on 2021-06-20 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobsDB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobinfo',
            name='source',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
