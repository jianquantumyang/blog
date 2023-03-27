from django import forms
from .models import *
# формы не связанные с Model
# class AddPostForm(forms.Form):000101101011011
#     title = forms.CharField(max_length=255,label="Заголовок",widget=forms.TextInput(attrs={'class':'form-control'}))
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10,"class":"form-control"}),label="Текст статьи")
#     photo = forms.ImageField(label="Фото")
#     is_published = forms.BooleanField(label="Публиковать",required=False,initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(),label='Категории',empty_label="Категория не выбрана")

class AddPostForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Blog
        fields = ["title",'content','photo','is_published','cat']
        widgets = {
            'title':forms.TextInput(attrs={'class':"form-control"}),
            'content':forms.Textarea(attrs={'class':"form-control"}),


        }


class AddCategoryForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control'})
        }
