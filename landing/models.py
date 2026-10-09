from django.db import models


class Service(models.Model):
    """Услуга: установка сигнализации, автозапуск и т.д."""
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена, ₽', max_digits=10, decimal_places=0, blank=True, null=True)
    icon = models.CharField(
        'Emoji (запасной вариант)',
        max_length=10,
        blank=True,
        default='🔧',
        help_text='Показывается, если не загружена картинка'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='services/',
        blank=True,
        null=True,
        help_text='PNG, JPG или SVG. Рекомендуемый размер: 200x200'
    )
    order = models.PositiveIntegerField('Порядок вывода', default=0)
    is_active = models.BooleanField('Показывать на сайте', default=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


class Review(models.Model):
    """Отзыв клиента"""
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Текст отзыва')
    rating = models.PositiveSmallIntegerField('Оценка (1-5)', default=5)
    car = models.CharField('Автомобиль', max_length=100, blank=True)
    created_at = models.DateTimeField('Дата', auto_now_add=True)
    is_published = models.BooleanField('Опубликован', default=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.rating}★'


class WorkExample(models.Model):
    """Пример работы — фото + подпись"""
    title = models.CharField('Название', max_length=200)
    description = models.CharField('Короткое описание', max_length=300, blank=True)
    image = models.ImageField('Фото', upload_to='works/')
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Показывать', default=True)

    class Meta:
        verbose_name = 'Пример работы'
        verbose_name_plural = 'Примеры работ'
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


class ContactRequest(models.Model):
    """Заявка с формы"""
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=30)
    message = models.TextField('Комментарий', blank=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    is_processed = models.BooleanField('Обработана', default=False)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.phone}'


class SiteSettings(models.Model):
    """Настройки сайта — редактируются в админке (одна запись)"""
    company_name = models.CharField('Название компании', max_length=200, default='Автосигнализации')
    phone = models.CharField('Телефон', max_length=30, default='+7 (___) ___-__-__')
    address = models.CharField('Адрес', max_length=300, blank=True)
    work_hours = models.CharField('Часы работы', max_length=200, blank=True, default='Ежедневно 9:00–21:00')
    hero_title = models.CharField('Заголовок на главной', max_length=300,
                                  default='Установка автосигнализаций с гарантией')
    hero_subtitle = models.TextField('Подзаголовок', blank=True,
                                     default='Профессионально, быстро, с гарантией до 3 лет')
    about = models.TextField('О компании', blank=True)

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self):
        return self.company_name