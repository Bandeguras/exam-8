from django import forms
from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'avatar']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['description', 'rating']


class ReviewFormModerator(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['description', 'rating', 'moderated']

