from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Payment(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_payments",
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True, default="")

    def __str__(self):
        return f"{self.sender} paid {self.receiver} ${self.amount} on {self.date}"
