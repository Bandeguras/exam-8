from django.shortcuts import get_object_or_404
from django.urls import reverse
from webapp.models import Product, Review
from webapp.form import ReviewForm
from django.views.generic import CreateView, UpdateView


class ProductReviewCreateView(CreateView):
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


class ReviewUpdateView(UpdateView):
    template_name = 'review/review_update.html'
    model = Review
    form_class = ReviewForm
    # context_object_name = 'comment'

    def get_success_url(self):
        return reverse('webapp:product', kwargs={'pk': self.object.product.pk})
