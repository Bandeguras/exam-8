
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.models import Product

from django.views.generic import RedirectView, ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductIndexViews(ListView):
    template_name = 'product/index.html'
    context_object_name = 'products'
    model = Product
    # ordering = ('-created_at',)

#
# class ArticleView(DetailView):
#     template_name = 'article/article_view.html'
#     model = Article
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         article = self.object
#         comments = article.comments.order_by('-created_at')
#         context['comments'] = comments
#         return context
#
#
# class MyRedirectView(RedirectView):
#     url = 'https://ccbv.co.uk/projects/Django/4.1/django.views.generic.base/RedirectView/'
#
#
# class ArticleCreateView(LoginRequiredMixin, CreateView):
#     template_name = "article/article_create.html"
#     model = Article
#     form_class = ArticleForm
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     # def dispatch(self, request, *args, **kwargs):
#     #     if not request.user.is_authenticated:
#     #         return redirect('accounts:login')
#     #     if not request.user.has_perm('webapp.add_article'):
#     #         raise PermissionDenied
#     #     return super().dispatch( request, *args, **kwargs)
#
#
#
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
