# Generated by Django 4.2.2 on 2023-07-02 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Состояние доставки',
                'verbose_name_plural': 'Состояния доставок',
            },
        ),
    ]