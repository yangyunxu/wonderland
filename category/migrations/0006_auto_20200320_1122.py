# Generated by Django 2.1.5 on 2020-03-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_auto_20200319_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='rate',
            field=models.CharField(default='10', max_length=20),
        ),
    ]
