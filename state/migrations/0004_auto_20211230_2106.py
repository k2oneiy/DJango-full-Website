# Generated by Django 3.2 on 2021-12-31 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0003_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ptitle', models.CharField(max_length=100)),
                ('Pname', models.CharField(max_length=200)),
                ('Pdatetime', models.DateField()),
                ('Pemail', models.EmailField(max_length=50)),
                ('Psubject', models.CharField(max_length=200)),
                ('Pmessage', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='time',
        ),
    ]
