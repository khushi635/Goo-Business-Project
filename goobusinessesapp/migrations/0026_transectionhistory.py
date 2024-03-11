# Generated by Django 5.0 on 2024-02-10 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goobusinessesapp', '0025_callingconverssiontrack'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransectionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slID', models.IntegerField(blank=True, default=0, null=True)),
                ('fullname', models.CharField(default='', max_length=122)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.CharField(default='', max_length=20)),
                ('payment', models.BooleanField(default=False)),
                ('paymentStatus', models.CharField(blank=True, max_length=30, null=True)),
                ('paymentAmount', models.IntegerField(blank=True, default=0, null=True)),
                ('lastUpdateTime', models.TimeField(auto_now=True)),
                ('lastUpdatedate', models.DateField(auto_now=True)),
                ('acceptTime', models.TimeField(auto_now_add=True)),
                ('acceptdate', models.DateField(auto_now_add=True)),
                ('razorpay_payment_iddb', models.CharField(max_length=150)),
                ('razorpay_order_iddb', models.CharField(max_length=150)),
                ('razorpay_signaturedb', models.CharField(max_length=150)),
            ],
        ),
    ]