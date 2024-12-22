# Generated by Django 5.1.4 on 2024-12-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='date_posted',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]