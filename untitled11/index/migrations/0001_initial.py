# Generated by Django 2.2.5 on 2019-09-30 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inadmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=8)),
                ('email', models.CharField(max_length=50, null=True)),
                ('lasttime', models.DateTimeField(null=True)),
                ('registtime', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='inmenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuname', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='innews_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsid', models.PositiveSmallIntegerField(max_length=5)),
                ('content', models.TextField(max_length=640)),
                ('newstime', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'news_content',
            },
        ),
        migrations.CreateModel(
            name='inposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionname', models.PositiveSmallIntegerField(max_length=5)),
            ],
            options={
                'db_table': 'inposition',
            },
        ),
        migrations.CreateModel(
            name='inposition_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionid', models.PositiveSmallIntegerField(max_length=5)),
                ('newsid', models.PositiveSmallIntegerField(max_length=5)),
            ],
            options={
                'db_table': 'inposition_content',
            },
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catid', models.PositiveSmallIntegerField(max_length=5)),
                ('title', models.CharField(max_length=8)),
                ('title_font_colour', models.CharField(max_length=8, null=True)),
                ('thumb', models.CharField(max_length=64, null=True)),
                ('num', models.PositiveSmallIntegerField(max_length=5)),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]
