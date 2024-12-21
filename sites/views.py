from django.shortcuts import render, redirect
from .models import Atividade
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.paginator import Paginator

def home(request):
    return render(request, "sites/index.html")

def index(request):
    return render(request, 'index.html')
@login_required
def atividades(request):
    atividade_list = Atividade.objects.all()
    paginator = Paginator(atividade_list, 4)  # 4 atividades por página
    page_number = request.GET.get('page')
    atividades = paginator.get_page(page_number)
    return render(request, 'atividades.html', {'atividades': atividades})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  
            else:
                form.add_error(None, "Usuário ou senha inválidos")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def cadusuario_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('home')  
        else:
            messages.error(request, 'Erro ao registrar o usuário. Verifique os campos e tente novamente.')
    else:
        form = UserCreationForm()  
    return render(request, 'cadusuario.html', {'form': form})