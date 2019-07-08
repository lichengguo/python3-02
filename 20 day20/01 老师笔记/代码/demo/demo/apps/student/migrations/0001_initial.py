# Generated by Django 2.2.2 on 2019-06-23 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='姓名')),
                ('sex', models.SmallIntegerField(choices=[(1, '男'), (2, '女'), (3, '保密')], default=3, verbose_name='性别')),
                ('class_no', models.IntegerField(db_column='class', verbose_name='班级')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('description', models.TextField(null=True, verbose_name='个性签名')),
                ('status', models.SmallIntegerField(verbose_name='是否删除')),
                ('orders', models.IntegerField(default=None, null=True, verbose_name='排序')),
            ],
            options={
                'verbose_name': '学生信息表',
                'verbose_name_plural': '学生信息表',
                'db_table': 'student',
            },
        ),
    ]
