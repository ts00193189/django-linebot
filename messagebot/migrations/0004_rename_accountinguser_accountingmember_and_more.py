# Generated by Django 4.0.3 on 2022-04-22 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messagebot', '0003_rename_record_accountingrecord_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccountingUser',
            new_name='AccountingMember',
        ),
        migrations.AlterModelTable(
            name='accountingmember',
            table='accounting_member',
        ),
        migrations.AlterModelTable(
            name='accountingrecord',
            table='accounting_record',
        ),
        migrations.AlterModelTable(
            name='accountingtype',
            table='accounting_type',
        ),
    ]