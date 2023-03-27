from django.urls import reverse_lazy,reverse
from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255,verbose_name="Заголовок")
    content = models.TextField(blank=True,verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/",verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True,verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True,verbose_name="Публикирован?")
    cat = models.ForeignKey('Category',on_delete=models.PROTECT,null=True,verbose_name="Катеогория")
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse_lazy('index')
    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=127,db_index=True,verbose_name="Название")
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category',kwargs={'cat':self.pk})
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']
