from rest_framework import serializers

from product.models import Product, Lesson, UserLesson


class ProductSerializer(serializers.ModelSerializer):
    total_views = serializers.ReadOnlyField()
    total_time_viewed = serializers.ReadOnlyField()
    total_students = serializers.ReadOnlyField()
    acquisition_percentage = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ('id', 'name_product', 'owner', 'total_views',
                  'total_time_viewed', 'total_students', 'acquisition_percentage')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'name', 'url', 'duration')


class UserLessonSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    
    class Meta:
        model = UserLesson
        fields = ('id', 'lesson', 'viewed_time', 'status')


class UserLessonProductSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    last_viewed_date = serializers.DateTimeField()
    
    class Meta:
        model = UserLesson
        fields = ('id', 'lesson', 'viewed_time', 'status', 'last_viewed_date')
