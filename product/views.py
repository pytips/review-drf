from django.shortcuts import render
from rest_framework import generics
from .models import Product, ProductReview
from .serializers import (ProductListSerializer, ReviewListSerializer,
                          ReviewCreateSerializer, ReviewUpdateSerializer,
                          ReviewDeleteSerializer)
from django.db.models.functions import Coalesce
from django.db.models import Avg, IntegerField
from rest_framework.permissions import IsAuthenticated
from .permission import ObjectPermission


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        return Product.objects.annotate(avg_rating=Coalesce(Avg("productreview__rating"), 0,
                                                            output_field=IntegerField()))


class ReviewListView(generics.ListAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ReviewListSerializer


class ReviewCreateView(generics.CreateAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ReviewUpdateView(generics.UpdateAPIView):
    serializer_class = ReviewUpdateSerializer
    permission_classes = (IsAuthenticated, ObjectPermission)
    lookup_field = "id"

    def get_queryset(self):
        return ProductReview.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class ReviewDeleteView(generics.DestroyAPIView):
    serializer_class = ReviewDeleteSerializer
    permission_classes = (IsAuthenticated, ObjectPermission)
    lookup_field = "id"

    def get_queryset(self):
        return ProductReview.objects.filter(user=self.request.user)
