# Generated by Django 3.0.5 on 2022-04-19 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meanings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=100, unique=True)),
                ('meaning', models.CharField(max_length=300)),
            ],
        ),
    ]
