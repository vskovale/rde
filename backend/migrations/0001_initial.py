# Generated by Django 5.0.6 on 2024-07-12 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slides/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='backend.slider')),
            ],
        ),
    ]
