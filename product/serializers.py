from rest_framework import serializers
from .models import Product, ProductReview


class ProductListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {
            "avg_rating": {"read_only": True}
        }


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = "__all__"


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ("product", "rating", "review_text", )


class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ("rating", "review_text")


class ReviewDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ("id", )
