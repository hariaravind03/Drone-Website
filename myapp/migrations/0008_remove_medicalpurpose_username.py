# Generated by Django 5.0.4 on 2024-10-04 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_medicalpurpose_username_alter_medicalpurpose_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalpurpose',
            name='username',
        ),
    ]