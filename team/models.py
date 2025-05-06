from django.db import models

# Create your models here.
class Team(models.Model):
    full_name = models.CharField(max_length=100)
    github_link = models.URLField(max_length=200, blank=True, null=True)
    linkedin_link = models.URLField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='team/images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Jamoa a'zolari"
        verbose_name_plural = "Jamoa a'zolari"
        ordering = ['-created_at']
        
