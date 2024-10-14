# Generated by Django 4.0.6 on 2024-10-14 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waitlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('question', models.CharField(max_length=5000, null=True)),
                ('response', models.CharField(max_length=5000)),
                ('responded', models.BooleanField(default=False)),
                ('time_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Email',
        ),
    ]
