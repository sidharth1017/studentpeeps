# Generated by Django 3.2.5 on 2021-11-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
