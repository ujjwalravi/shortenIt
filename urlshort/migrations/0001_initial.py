# Generated by Django 3.2.8 on 2021-11-20 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlShort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.URLField(null=True)),
                ('short', models.CharField(max_length=50, null=True, unique=True)),
                ('visits', models.PositiveIntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]