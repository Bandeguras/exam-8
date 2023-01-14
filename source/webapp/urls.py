from django.urls import path
from webapp.views import ProductIndexViews, ProductView, ProductCreateView


app_name = 'webapp'

urlpatterns = [
    path('', ProductIndexViews.as_view(), name='product_index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
]