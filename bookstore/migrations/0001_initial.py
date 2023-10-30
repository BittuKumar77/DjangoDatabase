# Generated by Django 4.2.6 on 2023-10-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('best_seller', models.BooleanField(default=False)),
            ],
        ),
    ]
