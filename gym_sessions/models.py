from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

User = get_user_model()


class GymSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True, default="")

    class Meta:
        ordering = ("-date",)
        verbose_name = "Gym Session"
        verbose_name_plural = "Gym Sessions"

    def __str__(self):
        return f"Session on {self.date.strftime('%Y-%m-%d %H:%M')} by {self.user}"

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)

    def clean(self):
        error_message = "You can't create more than one GymSession in one day."
        # Check if a GymSession already exists for this user today
        start_of_day = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_day = start_of_day + timezone.timedelta(days=1)
        if GymSession.objects.filter(
            user=self.user,
            date__range=(start_of_day, end_of_day),
        ).exists():
            raise ValidationError(
                error_message,
            )


class GymSessionImage(models.Model):
    session = models.ForeignKey(
        GymSession,
        related_name="images",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="gym_sessions/")
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-upload_date",)
        verbose_name = "Gym Session Image"
        verbose_name_plural = "Gym Session Images"

    def __str__(self):
        return f"Image for session on {self.session.date.strftime('%Y-%m-%d %H:%M')} uploaded on {self.upload_date.strftime('%Y-%m-%d %H:%M')}"  # noqa: E501
