from django.db import models
from django.conf import settings


class Deal(models.Model):

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('FUNDS_HELD', 'Funds Held'),
        ('COMPLETED', 'Completed'),
        ('DISPUTED', 'Disputed'),
    )

    title = models.CharField(max_length=255)

    description = models.TextField()

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='seller_deals'
    )

    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='buyer_deals',
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title