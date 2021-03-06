# Generated by Django 2.1.1 on 2019-01-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('keyword', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EditSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('keyword', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=100)),
            ],
        ),
    ]
