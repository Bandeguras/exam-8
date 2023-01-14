from django.urls import path
from webapp.views import ProductIndexViews, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ProductReviewCreateView, ReviewUpdateView, ReviewDeleteView


app_name = 'webapp'

urlpatterns = [
    path('', ProductIndexViews.as_view(), name='product_index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/review/', ProductReviewCreateView.as_view(), name='product_review'),
    path('product/<int:pk>/review/update/', ReviewUpdateView.as_view(), name='product_review_update'),
    path('product/<int:pk>/review/delete/', ReviewDeleteView.as_view(), name='product_review_delete'),

]