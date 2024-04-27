from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class GymSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True, default="")

    def __str__(self):
        return (
            f"Session on {self.date.strftime('%Y-%m-%d %H:%M')} by {self.user.username}"
        )


class GymSessionImage(models.Model):
    session = models.ForeignKey(
        GymSession,
        related_name="images",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="gym_sessions/")
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for session on {self.session.date.strftime('%Y-%m-%d %H:%M')} uploaded on {self.upload_date.strftime('%Y-%m-%d %H:%M')}"  # noqa: E501
