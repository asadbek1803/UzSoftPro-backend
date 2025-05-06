from django.db import models

# Create your models here.
class Orders(models.Model):
    BUDGET_CHOICES = [
        ('5-million-so\'mgacha', '5 million so\'m'),
        ('5-10-million-so\'m', '5-10 million so\'m'),
        ('10-20-million-so\'m', '10-20 million so\'m'),
        ('20-50-million-so\'m', '20-50 million so\'m'),
        ('50-million-so\'mdan-yuqori', '50 million so\'mdan yuqori'),
        ('boshqa', 'Boshqa'),
    ]
    PRODUCTS = [
        ('web-sayt-yaratish', 'Web sayt yaratish'),
        ('mobil-ilova-yaratish', 'Mobil ilova yaratish'),
        ('seo-xizmatlari', 'SEO xizmatlari'),
        ('digital-marketing', 'Digital marketing'),
        ('brending', 'Brending'),
        ('grafik-dizayn', 'Grafik dizayn'),
        ('video-tahrirlash', 'Video tahrirlash'),
        ('kontent-yaratish', 'Kontent yaratish'),
        ('smm', 'SMM'),
        ('onlayn-kurslar', 'Onlayn kurslar'),
        ('telegram-bot', 'Telegram bot'),
        ('boshqa', 'Boshqa'),
    ]
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    product = models.CharField(max_length=200, choices=PRODUCTS)
    product_description = models.TextField()
    budget = models.CharField(max_length=50, choices=BUDGET_CHOICES)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} by {self.customer_name}"