from django.urls import path
from .views import ProductListCreateAPIView, ProductDetailAPIView, CategoryListCreateAPIView, CategoryDetailAPIView, CategoryProductsListAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('categories/<int:id>/products/', CategoryProductsListAPIView.as_view(), name='category-products'),
]