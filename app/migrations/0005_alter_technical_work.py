# Generated by Django 3.2.4 on 2023-10-12 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_technical_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technical',
            name='work',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='内容'),
        ),
    ]
