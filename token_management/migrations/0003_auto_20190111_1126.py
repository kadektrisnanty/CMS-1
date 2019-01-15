# Generated by Django 2.1.3 on 2019-01-11 04:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('token_management', '0002_auto_20190111_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='token',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]