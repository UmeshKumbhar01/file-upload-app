# Generated by Django 5.0.1 on 2024-01-29 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_handling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.DeleteModel(
            name='MyTable',
        ),
    ]
