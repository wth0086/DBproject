# Generated by Django 3.1.3 on 2020-12-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='complain_code',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
