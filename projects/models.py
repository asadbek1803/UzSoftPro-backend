from django.db import models



# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriyalar"
        verbose_name_plural = "Kategoriyalar"
        ordering = ['-created_at']


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)
    github_link = models.URLField(max_length=200, blank=True, null=True)
    live_link = models.URLField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Loyihalar"
        verbose_name_plural = "Loyihalar"
        ordering = ['-created_at']