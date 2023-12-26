from django import forms
from django.db import models


# Create your models here.
class Registration(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)  # Adjust the max length accordingly
    confirm_password = models.CharField(max_length=255)


def _str_(self):
    return self.username


class District(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    wikipedia_link = models.URLField()

    def _str_(self):
        return self.name


class AccountType(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name


class Personnal(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    phonenumber = models.CharField(max_length=10,null=False)
    mailid = models.EmailField(null=False)
    address = models.TextField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    AccountType = models.ForeignKey(AccountType, on_delete=models.CASCADE,
                                     choices=[('savings Account', 'Savings account'),
                                              ('current account', 'Current account'),
                                              ('other', 'Other')])
    materials_provide1 = models.CharField(max_length=100)
    materials_provide2 = models.CharField(max_length=100)
    materials_provide3 = models.CharField(max_length=100)

    def _str_(self):
        return self.name
