# Generated by Django 4.0.3 on 2022-04-22 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messagebot', '0002_auto_20220420_1748'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Record',
            new_name='AccountingRecord',
        ),
        migrations.RenameModel(
            old_name='Type',
            new_name='AccountingType',
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='AccountingUser',
        ),
    ]