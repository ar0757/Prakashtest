# Generated by Django 4.2.1 on 2023-05-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='volunteer_profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteer_no', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=20)),
                ('ngo_association', models.CharField(max_length=100)),
                ('area_of_operation', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Volunteer Profile',
            },
        ),
    ]
