from django.shortcuts import render
from rest_framework import generics, authentication, permissions


from rest_framework import viewsets
from product.models import Product, UserLesson
from .serializers import (UserLessonSerializer, ProductSerializer,
                          UserLessonProductSerializer)


class ListUserLessonAPIView(generics.ListAPIView):
    serializer_class = UserLessonSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        products = Product.objects.filter(productuser__user=user,
                                          productuser__accsess_user=True)
        return UserLesson.objects.filter(lesson__products__in=products)


class UserLessonOfProductViewSet(viewsets.ModelViewSet):
    serializer_class = UserLessonProductSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.request.query_params.get('product_id')
        if product_id is not None:
            return UserLesson.objects.filter(user=user,
                                             lesson__products__id=product_id)
        else:
            return UserLesson.objects.filter(user=user)


class ProductStatisticAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        products = Product.objects.all()
        return products
