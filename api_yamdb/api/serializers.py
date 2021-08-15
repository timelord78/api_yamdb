from rest_framework import serializers


from reviews.models import Title, Comment, Review


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Review
        fields = '__all__'