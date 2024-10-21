from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post, Comentario
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from .forms import PostForm
from django.shortcuts import render, redirect
import re  




def index(request):
    return render(request, 'blog/index.html')



def lista_posts(request):
    posts = Post.objects.all().order_by('-id')  
    return render(request, 'blog/lista_posts.html', {'posts': posts}) 





from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseBadRequest
from .models import Post, Comentario  

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = post.comentarios.all()

    
    if request.method == 'POST':
        if request.user.is_authenticated:
            contenido = request.POST.get('contenido')
            
            if contenido and contenido.strip():  
                Comentario.objects.create(
                    post=post,
                    autor=request.user,
                    contenido=contenido
                )
                return redirect('blog:detalle_post', post_id=post.id)  
            else:
                return HttpResponseBadRequest("El comentario no puede estar vacío.") 

    
    return render(request, 'blog/detalle_post.html', {'post': post, 'comentarios': comentarios})







def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if not username or not password or not password_confirm:
            messages.error(request, 'Por favor, complete todos los campos.')
            return redirect('blog:register')
        
        if password != password_confirm:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('blog:register')
        
        if len(password) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres.')
            return redirect('blog:register')

        
        if not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password):
            messages.error(request, 'La contraseña debe contener al menos una letra y un número.')
            return redirect('blog:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
            return redirect('blog:register')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('blog:lista_posts')

    return render(request, 'blog/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Por favor, ingrese usuario y contraseña.')
            return redirect('blog:login')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '¡Bienvenido!')
            return redirect('blog:lista_posts')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'blog/login.html')


def logout_view(request):
    logout(request)
    return redirect('blog:lista_posts')



@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user  
            post.save()
            return redirect('blog:lista_posts')
    else:
        form = PostForm()
    
    return render(request, 'blog/crear_post.html', {'form': form})



@login_required
def agregar_comentario(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        
        
        if contenido and contenido.strip():
            Comentario.objects.create(
                post=post,
                autor=request.user,  
                contenido=contenido
            )
            return redirect('blog:detalle_post', post_id=post.id)
        else:
            return HttpResponseBadRequest("El comentario no puede estar vacío.")
    
    return redirect('blog:detalle_post', post_id=post.id)
