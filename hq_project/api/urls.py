from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ListUserLessonAPIView, UserLessonOfProductViewSet, ProductStatisticAPIView
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'user-lessons', UserLessonOfProductViewSet, basename='user-product-lessons')

urlpatterns = [
    path('', include(router.urls)),
    path('lessons/', ListUserLessonAPIView.as_view(), name='user-lessons'),
    path('product_stats/', ProductStatisticAPIView.as_view(), name='product_stats'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)