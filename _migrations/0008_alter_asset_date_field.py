# Generated by Django 3.2 on 2021-05-04 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MKsystemApp', '0007_alter_user_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='date_field',
            field=models.DateField(null=True),
        ),
    ]
