from django.urls import path
from . import views


urlpatterns = [
    path('product-list/', views.ProductListView.as_view()),

    path('review-list/', views.ReviewListView.as_view()),
    path('review-create/', views.ReviewCreateView.as_view()),
    path('review-update/<int:id>/', views.ReviewUpdateView.as_view()),
    path('review-delete/<int:id>/', views.ReviewDeleteView.as_view()),
]