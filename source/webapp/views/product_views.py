
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.models import Product
from webapp.form import ProductForm
from django.views.generic import RedirectView, ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductIndexViews(ListView):
    template_name = 'product/index.html'
    context_object_name = 'products'
    model = Product
    # ordering = ('-created_at',)


class ProductView(DetailView):
    template_name = 'product/product_view.html'
    model = Product


class ProductCreateView(CreateView):
    template_name = 'product/product_create.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('webapp:product_index')


# class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
#     template_name = "article/article_update.html"
#     form_class = ArticleForm
#     model = Article
#     context_object_name = 'article'
#     permission_required = 'webapp.change_article'
#
#     def has_permission(self):
#         return super().has_permission() or self.get_object().author == self.request.user
#
#     # def has_permission(self):
#     #     project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
#     #     return super().has_permission() and self.request.user in project.user.all()
#
#
# class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
#     template_name = 'article/article_delete.html'
#     model = Article
#     context_object_name = 'article'
#     success_url = reverse_lazy('index')
#     form_class = ArticleDeleteForm
#     permission_required = 'webapp.delete_article'
#
#     def has_permission(self):
#         return super().has_permission() or self.get_object().author == self.request.user
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.form_class(instance=self.object, data=request.POST)
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
