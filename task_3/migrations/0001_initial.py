# Generated by Django 4.2.2 on 2023-07-02 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=255)),
                ('available', models.BooleanField(default=True)),
                ('buyer', models.CharField(max_length=255)),
            ],
        ),
    ]
