# Generated by Django 3.2 on 2021-11-30 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerMore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=250, verbose_name='address')),
                ('Postal_code', models.IntegerField(blank=True, verbose_name='Postal code')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='C_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Consignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('weight', models.IntegerField(blank=True, verbose_name='weight')),
                ('package_type', models.CharField(choices=[('PALLET', 'Pallet'), ('BOX', 'Box'), ('BULK', 'Bulk'), ('CONTAINER', 'Container')], max_length=15, verbose_name='package type')),
                ('number', models.CharField(blank=True, max_length=20, verbose_name='number')),
                ('origin_of_sending', models.CharField(max_length=50, verbose_name='origin of sending')),
                ('recipient_destination', models.CharField(max_length=50, verbose_name='recipient destination')),
                ('recipient_name', models.CharField(max_length=50, verbose_name='recipient name')),
                ('recipient_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='phone_number')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consignment', to='customer.customermore')),
            ],
            options={
                'verbose_name': 'CustomerUser',
                'verbose_name_plural': 'CustomersUser',
            },
        ),
    ]
