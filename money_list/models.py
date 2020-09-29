from django.db import models

# Create your models here.

class MoneyTransaction(models.Model):
    num = models.AutoField(primary_key=True)
    user_num = models.ForeignKey('User', models.DO_NOTHING, db_column='user_num')
    entry_name = models.CharField(max_length=50, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def money_save(self):
        self.save()

    class Meta:
        managed = False
        db_table = 'money_transaction'


class User(models.Model):
    num = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=20)
    pwd = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'