import datetime

from django.db import models

# Create your models here.
class AccountingType(models.Model):
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'accounting_type'

    def __str__(self):
        return self.name


class AccountingMember(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'accounting_member'

    def __str__(self):
        return self.name


class AccountingRecord(models.Model):
    cost = models.IntegerField()
    note = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(default=datetime.date.today)
    member_id = models.ForeignKey(AccountingMember, on_delete=models.CASCADE, related_name='record')
    accounting_type_id = models.ForeignKey(AccountingType, null=True, on_delete=models.SET_NULL, related_name='record')

    class Meta:
        db_table = 'accounting_record'

    def __str__(self):
        return '{} {} {} {} {}'.format(self.cost, self.member_id, self.accounting_type_id, self.date, self.note)
