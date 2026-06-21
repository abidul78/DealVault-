from django.db import models
from deals.models import Deal


class Transaction(models.Model):

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('HELD', 'Held'),
        ('RELEASED', 'Released'),
        ('REFUNDED', 'Refunded'),
    )

    deal = models.OneToOneField(
        Deal,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id}"