# Generated by Django 2.2.5 on 2019-10-06 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20191006_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='inadmin',
            name='content',
            field=models.TextField(max_length=6400, null=True),
        ),
    ]
