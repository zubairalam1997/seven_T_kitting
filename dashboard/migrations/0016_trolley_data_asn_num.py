# Generated by Django 5.0.3 on 2024-06-05 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_trolley_data_trolley_picking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='trolley_data',
            name='asn_num',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]