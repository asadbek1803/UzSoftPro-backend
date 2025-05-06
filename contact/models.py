from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    theme = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Aloqa"
        verbose_name_plural = "Aloqalar"
        ordering = ['-created_at']