from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.models import Product, Review
from webapp.form import ProductForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin


class ProductIndexViews(ListView):
    template_name = 'product/index.html'
    context_object_name = 'products'
    model = Product
    # ordering = ('-created_at',)


class ProductView(DetailView):
    template_name = 'product/product_view.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        reviews = product.reviews.order_by('-created_at')
        context['reviews'] = reviews
        return context


class ProductCreateView(CreateView):
    template_name = 'product/product_create.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('webapp:product_index')


class ProductUpdateView(UpdateView):
    template_name = 'product/product_update.html'
    model = Product
    form_class = ProductForm


class ProductDeleteView(DeleteView):
    template_name = 'product/product_delete.html'
    model = Product
    success_url = reverse_lazy('webapp:product_index')

