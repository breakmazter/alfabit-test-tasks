from django.db import models

from utils.decorators import add_get_methods


@add_get_methods(field_prefix='STATE_')
class DeliveryState(models.Model):
    class Meta:
        verbose_name = 'Состояние доставки'
        verbose_name_plural = 'Состояния доставок'

    STATE_NEW = 1  # Новая
    STATE_ISSUED = 2  # Выдана курьеру
    STATE_DELIVERED = 3  # Доставлена
    STATE_HANDED = 4  # Курьер сдал
    STATE_REFUSED = 5  # Отказ
    STATE_PAID_REFUSED = 6  # Отказ с оплатой курьеру
    STATE_COMPLETE = 7  # Завершена
    STATE_NONE = 8  # Не определено
