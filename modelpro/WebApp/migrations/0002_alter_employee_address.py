# Generated by Django 4.2.1 on 2023-07-31 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
