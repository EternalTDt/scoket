from django.db import models


class Tag(models.Model):
    created_at = models.DateTimeField("Дата создания",auto_now_add=True)
    name = models.CharField("Название", max_length=60)
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    created_at = models.DateTimeField("Дата создания",auto_now_add=True)
    title = models.CharField("Заголовок", max_length=100, blank=True)
    body = models.TextField("Содержание", blank=True)
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True)
    image = models.ImageField("Изображение", upload_to='blog_images', blank=True)
    tags = models.ManyToManyField(
        Tag,
        verbose_name="Теги",
        related_name="posts",
        blank=True,
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['created_at']


class Comment(models.Model):
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    body = models.TextField("Содержание", blank=False)
    owner = models.ForeignKey('auth.User', verbose_name="Пользователь", related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', verbose_name="Пост", related_name='comments', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.owner.username}: {self.post.title}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['created_at']
