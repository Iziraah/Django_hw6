from django import forms# from django.template.context_processors import MinValueValidator
from .models import Product



class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)
    
# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     description = forms.CharField(widget=forms.Textarea)
#     price = forms.DecimalField(max_digits=10, decimal_places=2)
#     quantity = forms.IntegerField(initial=0)
#     image = forms.ImageField()

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'