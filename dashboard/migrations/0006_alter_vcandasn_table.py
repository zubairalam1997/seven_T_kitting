# Generated by Django 5.0.3 on 2024-04-06 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_vcandasn_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='vcandasn',
            table=('vc_and_asn',),
        ),
    ]
