from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.utils import timezone

# Create your models here.

def transaction_type_validate(value):
    """Validation for type field - can be I (income) or E (expense)"""

    if value != "I" and value != "E":
        raise ValidationError(_('%(value) can be only I (income) or E (expense).'), params={'value': value})


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(unique=True, max_length=255, db_index=True)
    # is_active = models.BooleanField(null=False)
    # is_staff = models

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Transaction(models.Model):
    """Model for FI transaction"""

    type_choices = [
        ('E', 'Expense'),
        ('I', 'Income'),
    ]

    date = models.DateField(blank=False, default=timezone.now)
    type = models.CharField(
        max_length=1,
        blank=False,
        null=False,
        validators=[transaction_type_validate],
        default='E',
        choices=type_choices,)
    amount = models.IntegerField(blank=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey('TransactionCategory', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{date} - {type} - {amount} - {descr}'.format(
            date = self.date,
            type = self.type,
            amount = self.amount,
            descr = self.description,
        )


class TransactionCategory(models.Model):
    """Model for Transaction category"""

    name = models.CharField(max_length=255, blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name