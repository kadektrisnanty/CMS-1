# Generated by Django 2.1.3 on 2019-01-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_management', '0003_auto_20190111_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='count_subject',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='token',
            name='list_subject',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
