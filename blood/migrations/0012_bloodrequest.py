# Generated by Django 5.0.6 on 2024-11-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0011_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('blood_type', models.CharField(choices=[('A+', 'A+'), ('O+', 'O+'), ('B+', 'B+'), ('AB+', 'AB+'), ('A-', 'A-'), ('O-', 'O-'), ('B-', 'B-'), ('AB-', 'AB-')], max_length=3)),
                ('hospital_address', models.TextField()),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='pending', max_length=10)),
            ],
        ),
    ]
