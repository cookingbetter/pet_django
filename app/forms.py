from django import forms
# from .models import Receipt
from .models import Post

# class ReceiptForm(forms.ModelForm):
#     class Meta:
#         model = Receipt
#         fields = ('name', 'type', 'cooking_time', 'img')


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'type', 'cooking_time', 'img']