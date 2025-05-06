from django.db import models

# Create your models here.
class Follower(models.Model):
    email = models.EmailField()
    is_subscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Foydalanuvchilar"
        verbose_name_plural = "Foydalanuvchilar"
        ordering = ['-created_at']