# Generated by Django 4.1.5 on 2023-02-01 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goobusinessesapp', '0007_controlweb_datetimevar'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSeenDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=50, null=True)),
                ('unicNum', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('lastSeen', models.DateField(auto_now=True)),
            ],
        ),
    ]
