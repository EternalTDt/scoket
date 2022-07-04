from django.db import models
from .product_models import Socket
from django.db.models import Avg



SOCKET_STARS = {
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
}


class SocketReview(models.Model):
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    body = models.TextField("Содержание", blank=False)
    owner = models.ForeignKey('auth.User', verbose_name="Пользователь", related_name='reviews', on_delete=models.CASCADE)
    sockets = models.ForeignKey(Socket, verbose_name="Розетки", related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField("Рейтинг", choices=SOCKET_STARS, default=5)


    def __str__(self) -> str:
        return f'{self.owner.username}: {self.sockets.name}'

    def get_average_rating(self):
        avg_list = list(SocketReview.objects.filter(sockets=self.sockets.id).values_list('rating', flat=True))
        print(avg_list)
        summ = sum(avg_list)
        length = len(avg_list)
        avg_rating = summ / length
        return avg_rating


    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзыв"
        ordering = ['created_at']