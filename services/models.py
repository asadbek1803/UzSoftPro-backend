from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Xizmatlar"
        verbose_name_plural = "Xizmatlar"
        ordering = ['-created_at']