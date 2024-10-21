import datetime
import uuid
from email.policy import default
from enum import unique

from django.db import models
from django.utils import timezone
from unicodedata import decimal


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text




def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Shop(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id=models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    shop=models.ForeignKey('Shop', on_delete=models.CASCADE,related_name='products')
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    pub_date=models.DateTimeField(default=timezone.now)
    expire_date=models.DateTimeField()


    def __str__(self):
        return self.name


    def is__expired(self):
        return timezone.now()> self.expire_date
