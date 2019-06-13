# Generated by Django 2.2.1 on 2019-06-11 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('realname', models.CharField(max_length=32)),
                ('nickname', models.CharField(max_length=32)),
                ('channel', models.CharField(max_length=4)),
                ('phone', models.CharField(max_length=32)),
                ('sex', models.TextField()),
                ('province_id', models.PositiveIntegerField()),
                ('city_id', models.PositiveIntegerField()),
                ('head_url', models.CharField(max_length=125)),
                ('login_secret', models.CharField(max_length=8)),
                ('money', models.FloatField()),
                ('creator', models.PositiveIntegerField()),
                ('creation', models.DateTimeField()),
            ],
            options={
                'db_table': 'account',
                'managed': False,
            },
        ),
    ]
