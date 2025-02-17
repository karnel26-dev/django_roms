from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('in_progress', 'Готовится'),
        ('paid', 'Готов'),
        ('completed', 'Завершен'),
        ('cancelled', 'Отменен'),
    ]

    table_number = models.PositiveIntegerField()
    items = models.ManyToManyField(MenuItem, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def save(self, *args, **kwargs):
        # Автоматически вычисляем общую стоимость заказа
        self.total_price = sum(item.price for item in self.items.all())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заказ {self.id} - Стол {self.table_number} - Статус: {self.get_status_display()}"