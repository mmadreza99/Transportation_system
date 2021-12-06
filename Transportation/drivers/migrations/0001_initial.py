# Generated by Django 3.2 on 2021-12-06 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('created_time', models.DateTimeField(verbose_name='create time')),
                ('validity_date', models.DateTimeField(default=10, verbose_name='validity date')),
                ('type', models.CharField(choices=[('P1', 'p1'), ('P2', 'p2'), ('P3', 'p3')], max_length=10, verbose_name='type')),
                ('image', models.ImageField(null=True, upload_to='Certificate', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='KartHoshmand',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('validity_date', models.DateTimeField(verbose_name='validity date')),
                ('create_time', models.DateTimeField(verbose_name='create time')),
                ('image', models.ImageField(null=True, upload_to='kart_hoshmand', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PICKUP', 'Pickup'), ('BOX_TRUCK', 'Box_truck'), ('FLATBED_TRUCK', 'flatbed_truck'), ('DUMP_TRUCK', 'Dump_truck'), ('TANK_TRUCK', 'Tank_truck'), ('CAR_TRANSPORT', 'Car_transport'), ('HEAVY', 'Heavy')], max_length=15, verbose_name='type')),
                ('registration_plate', models.CharField(max_length=8, verbose_name='registration plate')),
                ('id_insurance', models.IntegerField(verbose_name='id insurance')),
                ('image', models.ImageField(upload_to='truck', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='DriverMore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_of_birth', models.DateTimeField(null=True, verbose_name='birth')),
                ('place_of_birth', models.CharField(blank=True, max_length=50, verbose_name='place of birth')),
                ('address', models.TextField(blank=True, max_length=150, verbose_name='address')),
                ('Driver_licence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Driver', to='drivers.certificate')),
                ('kart_hoshmand', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='drivers.karthoshmand')),
                ('truck', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='drivers.truck')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='D_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'DriverUser',
                'verbose_name_plural': 'DriversUser',
            },
        ),
    ]
