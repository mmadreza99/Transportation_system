# Generated by Django 4.2 on 2023-06-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consignment',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='Consignment'),
        ),
    ]
