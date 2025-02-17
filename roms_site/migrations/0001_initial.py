# Generated by Django 5.1.6 on 2025-02-17 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.PositiveIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('comment', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'В ожидании'), ('paid', 'Оплачен'), ('in_progress', 'Готовится'), ('ready', 'Готов'), ('completed', 'Завершен'), ('cancelled', 'Отменен')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('items', models.ManyToManyField(related_name='orders', to='roms_site.menuitem')),
            ],
        ),
    ]
