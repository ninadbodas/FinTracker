# Create your models here.
from django.db import models

class Transaction(models.Model):
    TRANSACTION_CATEGORIES = [
        ('Groceries', 'Groceries'),
        ('Entertainment', 'Entertainment'),
        ('Transportation', 'Transportation'),
        # Add more categories as needed
    ]

    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=TRANSACTION_CATEGORIES)
    account = models.CharField(max_length=100)
    note = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.transaction_date} - {self.amount} - {self.category}"