# Generated by Django 2.2.13 on 2021-03-16 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0006_auto_20210214_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_message', models.CharField(max_length=500)),
                ('chatbot_message', models.CharField(max_length=500)),
            ],
        ),
    ]
