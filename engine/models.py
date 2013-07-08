from django.db import models
import datetime

# Create your models here.

class ClientAccount(models.Model):
    accountID = models.IntegerField(unique=True,max_length = 10)
    name = models.CharField(max_length = 10)

class TransRecord(models.Model):
    code = models.IntegerField(max_length = 10)
    date = models.DateTimeField(max_length = 10)
    dealAmount = models.IntegerField(max_length = 10)
    dealID = models.ForeignKey(ClientAccount)
    dealPrice = models.FloatField(max_length = 10)
    entrustID = models.IntegerField(unique=True, max_length = 10)
    tradeAccount = models.IntegerField(max_length = 10)
    #status = models.IntegerField(max_length=1)

class ClientTransRecord(models.Model):
    accountID = models.ForeignKey(ClientAccount)
    code = models.IntegerField(max_length = 10)
    amount = models.IntegerField(max_length = 10)

class Dealer(models.Model):
    name = models.CharField(unique=True,max_length = 10)
    password = models.CharField(max_length = 20)
