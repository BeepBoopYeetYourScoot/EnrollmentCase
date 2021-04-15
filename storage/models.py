from django.db import models


class Storage(models.Model):
    """
    Единичная ячейка для хранения перечня запасов
    """
    UNITS = (
        ('kg', 'Килограмм'),
        ('liter', 'Литров')
    )

    title = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    unit = models.CharField(max_length=100, choices=UNITS)
    price = models.PositiveIntegerField()
    date = models.DateField()

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'

    def __str__(self):
        return f'Запас ресурса {self.title}'
