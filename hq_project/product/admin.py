from django.contrib import admin

from .models import Product, User, Lesson, ProductUser, UserLesson


admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(ProductUser)
admin.site.register(UserLesson)
