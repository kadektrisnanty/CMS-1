# Generated by Django 2.1.3 on 2019-01-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socmed_crawler', '0002_auto_20190115_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='config_yaml',
            new_name='config_yaml_name',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='deploy_yaml',
            new_name='config_yaml_url',
        ),
        migrations.AddField(
            model_name='subject',
            name='deploy_yaml_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='deploy_yaml_url',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]
