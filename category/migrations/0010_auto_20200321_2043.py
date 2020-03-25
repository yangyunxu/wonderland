# Generated by Django 2.1.5 on 2020-03-21 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0004_userprofile_user'),
        ('category', '0009_auto_20200321_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myaccount.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='wonder',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='category.Page'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='category.Category'),
            preserve_default=False,
        ),
    ]