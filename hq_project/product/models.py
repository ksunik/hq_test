from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

MAX_LENGTH = 255


class Product(models.Model):
    name_product = models.CharField(max_length=MAX_LENGTH,
                            verbose_name='Название продукта')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Владелец')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name_product
    
    @property
    def total_views(self):
        return UserLesson.objects.filter(lesson__products=self).count()

    @property
    def total_time_viewed(self):
        return UserLesson.objects.filter(lesson__products=self).aggregate(models.Sum('viewed_time'))["viewed_time__sum"]

    @property
    def total_students(self):
        return User.objects.filter(userlesson__lesson__products=self).distinct().count()

    @property
    def acquisition_percentage(self):
        total_users = User.objects.count()
        access_count = ProductUser.objects.filter(product=self, accsess_user=True).count()

        if total_users == 0:
            return 0
        else:
            return (access_count / total_users) * 100


class Lesson(models.Model):
    products = models.ManyToManyField(Product,
                                      blank=False,
                                      verbose_name='Название продукта урока')
    name = models.CharField(max_length=MAX_LENGTH,
                            verbose_name='Название урока')
    url = models.URLField(max_length=MAX_LENGTH,
                            verbose_name='Ссылка на видео',
                            unique=True)
    duration = models.PositiveIntegerField(verbose_name='Длительность просмотра (в секундах)')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name


class ProductUser(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name='Название продукта')
    user = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Имя юзера')
    accsess_user = models.BooleanField(default=False,
                                       verbose_name='Есть доступ к продукту')
    
    class Meta:
        verbose_name = 'Продукт-Пользователь'
        verbose_name_plural = 'Продукты_Пользователи'

    def __str__(self):
        return f'{self.product}, {self.user}, {self.accsess_user}'


class UserLesson(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Имя пользователя')
    lesson = models.ForeignKey(Lesson,
                               on_delete=models.CASCADE,
                               verbose_name='Название урока')
    viewed_time = models.PositiveIntegerField(verbose_name='Фактическое время просмотра')
    status = models.BooleanField(default=False,
                                 verbose_name='статус Просмотрено')
    last_viewed_date = models.DateTimeField(auto_now=True,
                                            verbose_name='Дата последнего просмотра')

    class Meta:
        verbose_name = 'Урок-Пользователь'
        verbose_name_plural = 'Уроки_Пользователи'

    def __str__(self):
        return f'{self.lesson}, {self.user}, {self.viewed_time}, {self.status}'

    def calculate_status(self):
        total_duration = self.lesson.duration
        viewed_percentage = (self.viewed_time / total_duration) * 100
        if viewed_percentage >= 80:
            self.status = True
        else:
            self.status = False
        self.save()
