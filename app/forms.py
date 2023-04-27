from django import forms
from .models import Receipt


class ReceiptForm(forms.ModelForm):
    is_favorite = forms.BooleanField(required=False)

    class Meta:
        model = Receipt
        fields = ('name', 'type', 'cooking_time', 'img', 'instruction', 'user', 'is_favorite')
        
    