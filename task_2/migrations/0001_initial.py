# Generated by Django 4.2.2 on 2023-07-02 22:26

from django.db import migrations, models
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Имя')),
                ('state', django_fsm.FSMField(default='new', max_length=50, verbose_name='Состояние')),
            ],
        ),
        migrations.CreateModel(
            name='LeadState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('new', 'Новый'), ('in_progress', 'В работе'), ('postponed', 'Приостановлен'), ('done', 'Завершен')], max_length=50, unique=True, verbose_name='Название')),
            ],
        ),
    ]