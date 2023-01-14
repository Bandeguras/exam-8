from django.contrib.auth.forms import UserCreationForm
from django.forms import forms


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email is '':
            raise forms.ValidationError('Поля email обязательно')
        return email