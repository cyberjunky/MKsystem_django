# Generated by Django 3.2 on 2021-05-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MKsystemApp', '0008_alter_asset_date_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='date_field',
        ),
        migrations.AddField(
            model_name='asset',
            name='date',
            field=models.DateField(null=True, verbose_name='日付'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True, verbose_name='運用率'),
        ),
    ]
