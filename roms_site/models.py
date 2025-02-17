from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.price} руб.'


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('paid', 'Оплачен'),
        ('in_progress', 'Готовится'),
        ('ready', 'Готов'),
        ('completed', 'Завершен'),
        ('cancelled', 'Отменен'),
    ]

    table_number = models.PositiveIntegerField()
    items = models.ManyToManyField(MenuItem, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    comment = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Заказ {self.id} - Стол {self.table_number} - Статус: {self.get_status_display()}"