from django.shortcuts import get_object_or_404
from django.urls import reverse
from webapp.models import Product, Review
from webapp.form import ReviewForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class ReviewList(PermissionRequiredMixin, ListView):
    template_name = 'review/review_list.html'
    model = Review
    form_class = ReviewForm


class ProductReviewCreateView(LoginRequiredMixin, CreateView):
    template_name = 'review/review_create.html'
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('webapp:product', kwargs={'pk': self.object.product.pk})

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        form.instance.product = product
        form.instance.author = self.request.user
        return super().form_valid(form)



class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'review/review_update.html'
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('webapp:product', kwargs={'pk': self.object.product.pk})

    def has_permission(self):
        return self.request.user.has_perm('webapp.change_review') or self.get_object().author == self.request.user


class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    model = Review

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:product', kwargs={'pk': self.object.product.pk})

    def has_permission(self):
        return self.request.user.has_perm('webapp.delete_review') or self.get_object().author == self.request.user