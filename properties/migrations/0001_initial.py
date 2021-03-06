# Generated by Django 4.0.3 on 2022-03-27 19:24

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
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('price', models.FloatField(help_text='Per month')),
                ('bedroom_type', models.CharField(choices=[('SHARING', 'SHARING'), ('PRIVATE', 'PRIVATE')], default='PRIVATE', max_length=256)),
                ('bathroom_type', models.CharField(choices=[('SHARING', 'SHARING'), ('PRIVATE', 'PRIVATE'), ('COMMUNAL', 'COMMUNAL')], default='PRIVATE', max_length=256)),
                ('kitchen_type', models.CharField(choices=[('SHARING', 'SHARING'), ('PRIVATE', 'PRIVATE'), ('COMMUNAL', 'COMMUNAL')], default='PRIVATE', max_length=256)),
                ('campus', models.CharField(choices=[('DURBAN', 'DBN'), ('JOHANNESBURG', 'JHB'), ('CAPE TOWN', 'CPT')], default='JHB', max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
    ]
