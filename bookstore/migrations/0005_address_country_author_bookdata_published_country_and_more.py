# Generated by Django 4.2.6 on 2023-11-10 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_bookdata_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
            ],
            options={
                'verbose_name_plural': 'Author_Address',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookstore.address')),
            ],
        ),
        migrations.AddField(
            model_name='bookdata',
            name='published_country',
            field=models.ManyToManyField(to='bookstore.country'),
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='bookstore.author'),
        ),
    ]
