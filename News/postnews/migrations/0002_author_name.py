# Generated by Django 4.2.1 on 2023-06-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postnews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default='NoName', max_length=20),
        ),
    ]