from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido']

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo) < 5:
            raise forms.ValidationError("El título es muy corto.")
        return titulo

    def clean_contenido(self):
        contenido = self.cleaned_data.get('contenido')
        if len(contenido) < 20:
            raise forms.ValidationError("El contenido es muy corto.")
        return contenido
