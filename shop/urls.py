from django.urls import path
from shop import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('sell/', views.sell_view, name="sell"),
    path('vendor/', views.vendor_view, name="vendor"),
    path('products/<int:pk>/', views.product_detail, name="product_detail"),
]
