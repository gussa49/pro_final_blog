from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),  # Página principal (portada)
    path('blog/', views.lista_posts, name='lista_posts'),  # Lista de posts
    path('post/<int:post_id>/', views.detalle_post, name='detalle_post'),  # Detalle de cada post
    path('login/', views.login_view, name='login'),  # Página de login
    path('register/', views.register_view, name='register'),  # Página de registro
    path('logout/', views.logout_view, name='logout'),  # Cerrar sesión
    path('crear/', views.crear_post, name='crear_post'),  # Nueva ruta para crear un post
]
