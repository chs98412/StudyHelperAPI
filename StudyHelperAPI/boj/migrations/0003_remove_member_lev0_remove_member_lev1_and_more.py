# Generated by Django 4.1.5 on 2023-01-23 02:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boj', '0002_member_bojid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='lev0',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev1',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev10',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev11',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev12',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev13',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev14',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev15',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev16',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev17',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev18',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev19',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev2',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev20',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev21',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev22',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev23',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev24',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev25',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev26',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev27',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev28',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev29',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev3',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev30',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev4',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev5',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev6',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev7',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev8',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lev9',
        ),
        migrations.AddField(
            model_name='member',
            name='bojLev',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], size=None),
        ),
    ]