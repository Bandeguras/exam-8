from django.urls import path
from webapp.views import ProductIndexViews


app_name = 'webapp'

urlpatterns = [
    path('', ProductIndexViews.as_view(), name='product_index'),
]