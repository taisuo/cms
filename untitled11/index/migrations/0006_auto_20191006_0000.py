# Generated by Django 2.2.5 on 2019-10-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_inposition_content_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inposition_content',
            name='positionid',
            field=models.PositiveSmallIntegerField(max_length=5, null=True),
        ),
    ]