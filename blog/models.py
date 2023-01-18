import email
from email.policy import default
from enum import _auto_null
from inspect import GEN_CLOSED
from msilib.schema import PublishComponent
from optparse import Option
from pickle import FALSE
from random import choices
from tabnanny import verbose
from tokenize import blank_re
from django.db import models

class Gamepark(models.Model):
    gamepark_name = models.CharField(max_length = 50, verbose_name="gamepark_name")
    contact = models.CharField(max_length = 10)
    contact_person = models.CharField(max_length = 60)
    address = models.CharField(max_length=100, null=True, blank=True, default="null")

    def __str__(self):
        return self.gamepark_name

class Visitor(models.Model):
    GENDER_OPTIONS = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    visitor_name = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 2, choices = GENDER_OPTIONS)
    gamepark_id = models.ForeignKey(Gamepark, on_delete=models.CASCADE)
    age = models.IntegerField()
    contact = models.CharField(max_length = 11)
    address = models.CharField(max_length = 20)

    def __str__(self):
        return self.visitor_name

class Payment(models.Model):
    payment_date = models.DateField(auto_now = False)
    visitor_id = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    amount_paid = models.IntegerField()
    recieved_by = models.CharField(max_length=100, default="missing")

    def __str__(self):
        return self.amount_paid

class Warden(models.Model):
    warden_name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.warden_name} - {self.contact}"

class Wildlife_animal(models.Model):
    spices_type = models.CharField(max_length=40)
    no_of_spices = models.IntegerField()
    warden_id = models.ForeignKey(Warden, on_delete=models.CASCADE)
    recieved_by = models.CharField(max_length=100, default="missing")

    def __str__(self):
        #return f"{spices_type}-{warden_id}"
        return self.spices_type

    