# Generated by Django 3.0.7 on 2020-08-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='impression_store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impression', models.TextField()),
                ('time', models.TextField()),
            ],
        ),
    ]
