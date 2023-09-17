from django.db import models

class Watch(models.Model):
    CHOICES = [
        ('Спортивные', 'Спортивные'),
        ('классическое', 'Классическое'),
        ('Детское', 'Детское')
    ]

    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    category = models.CharField(max_length=50, null=True, choices=CHOICES)
    image = models.ImageField(upload_to='watches', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
