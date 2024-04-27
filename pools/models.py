from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Pool(models.Model):
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(User, related_name="pools")

    def __str__(self):
        return self.name


class Transaction(models.Model):
    pool = models.ForeignKey(
        Pool,
        on_delete=models.CASCADE,
        related_name="transactions",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="transactions_made",
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.amount}"
