# Generated by Django 5.0.4 on 2024-10-04 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_failmsg'),
    ]

    operations = [
        migrations.AddField(
            model_name='failmsg',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='failmsg',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
