# Generated by Django 3.2 on 2021-06-05 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MKsystemApp', '0012_withdrawal_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawal',
            name='status',
            field=models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='状況'),
        ),
    ]