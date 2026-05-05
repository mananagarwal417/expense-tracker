from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Transaction(models.Model):
    TYPES = (('Income', 'Income'), ('Expense', 'Expense'))
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TYPES)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.amount}"