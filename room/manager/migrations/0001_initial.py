# Generated by Django 3.0.3 on 2020-02-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField(null=True)),
                ('days', models.IntegerField(null=True)),
                ('check_in', models.DateTimeField(null=True)),
                ('check_out', models.DateTimeField(null=True)),
            ],
        ),
    ]
