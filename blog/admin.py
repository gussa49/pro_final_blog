from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'imagen')  
    search_fields = ['titulo']
    list_filter = ['fecha_publicacion']

    
    fieldsets = (
        (None, {
            'fields': ('titulo', 'contenido', 'imagen')  
        }),
    )

admin.site.register(Post, PostAdmin)
