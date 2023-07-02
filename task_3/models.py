from django.db import models, transaction

from utils.email import send_email_to_user_of_buy_product


class Product(models.Model):
    item_id = models.CharField(max_length=255)
    available = models.BooleanField(default=True)
    buyer = models.CharField(max_length=255)

    @classmethod
    def buy(cls, user, item_id):
        # Для целостности операции покупки и избежания ситуации когда человек заплатил за товар который уже купил кто-то
        # другой, необходимо использовать блокировку для обеспечения атомарности операций.
        with transaction.atomic():
            if not Product.objects.filter(item_id=item_id, available=True).exists():
                return False

            # Получаем продукт и блокируем доступ всем кроме текущей транзакции.
            product = Product.objects.select_for_update().filter(item_id=item_id, available=True).first()

            # В методе withdraw нужно прописать проверку на то, чтобы у юзера было достаточно среддств, если нет то
            # нужно отвлавливать исключения. Или могут возникнуть ошибки с сетью и т.д.
            user.withdraw(product.price)

            # Лучше сделать отправку сообщения в фоне, так чтобы она не блокировала покупку товара. Такое можно сделать
            # используя например celery задачу которая будет отправлять уведолмения о покупке и т.д
            send_email_to_user_of_buy_product(user=user)

            product.available = False
            product.buyer = user
            product.save()

            return True
