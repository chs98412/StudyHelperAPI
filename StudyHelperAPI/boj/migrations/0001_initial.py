# Generated by Django 4.1.5 on 2023-01-21 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channelId', models.IntegerField()),
                ('memberId', models.IntegerField()),
                ('setLevel', models.IntegerField()),
                ('setGoal', models.IntegerField()),
                ('lev0', models.IntegerField(default=0)),
                ('lev1', models.IntegerField(default=0)),
                ('lev2', models.IntegerField(default=0)),
                ('lev3', models.IntegerField(default=0)),
                ('lev4', models.IntegerField(default=0)),
                ('lev5', models.IntegerField(default=0)),
                ('lev6', models.IntegerField(default=0)),
                ('lev7', models.IntegerField(default=0)),
                ('lev8', models.IntegerField(default=0)),
                ('lev9', models.IntegerField(default=0)),
                ('lev10', models.IntegerField(default=0)),
                ('lev11', models.IntegerField(default=0)),
                ('lev12', models.IntegerField(default=0)),
                ('lev13', models.IntegerField(default=0)),
                ('lev14', models.IntegerField(default=0)),
                ('lev15', models.IntegerField(default=0)),
                ('lev16', models.IntegerField(default=0)),
                ('lev17', models.IntegerField(default=0)),
                ('lev18', models.IntegerField(default=0)),
                ('lev19', models.IntegerField(default=0)),
                ('lev20', models.IntegerField(default=0)),
                ('lev21', models.IntegerField(default=0)),
                ('lev22', models.IntegerField(default=0)),
                ('lev23', models.IntegerField(default=0)),
                ('lev24', models.IntegerField(default=0)),
                ('lev25', models.IntegerField(default=0)),
                ('lev26', models.IntegerField(default=0)),
                ('lev27', models.IntegerField(default=0)),
                ('lev28', models.IntegerField(default=0)),
                ('lev29', models.IntegerField(default=0)),
                ('lev30', models.IntegerField(default=0)),
            ],
        ),
    ]
