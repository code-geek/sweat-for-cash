from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Pool(models.Model):
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(User, related_name="pools")

    def __str__(self):
        return self.name
