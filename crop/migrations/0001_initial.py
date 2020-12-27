# Generated by Django 3.1.4 on 2020-12-27 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('feature1', models.CharField(max_length=255)),
                ('feature2', models.BooleanField()),
                ('feature3', models.DecimalField(decimal_places=10, max_digits=19)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'crop',
                'managed': True,
            },
        ),
    ]
