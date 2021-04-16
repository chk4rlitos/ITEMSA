from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView,  FormView,   TemplateView
from django.shortcuts import redirect
from .forms import LoginForm
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login as register_login, logout
from django.contrib import messages
from .models import Persona

# Create your views here.


class Dashboard(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **context):
        context['user'] = self.kwargs['pk']
        return super(Dashboard, self).get_context_data(**context)

def user_logout(request):
    logout(request)
    return redirect('login')


class ListPersonal(ListView):
    template_name = 'persona/lista_persona.html'
    paginate_by = 20
    model = Persona
    context_object_name = 'usuario'


    def get_queryset(self):
        queryset = super(ListPersonal, self).get_queryset()
        return queryset

    def get_context_data(self, **context):
        return super(ListPersonal, self).get_context_data(**context)
    

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard', request.user.id)
    login_form = LoginForm(request.POST or None)

    if request.method.upper() == 'POST' and login_form.is_valid():
        usuario = request.POST['nick']
        clave = request.POST['llave']
        user = authenticate(username=usuario, password=clave)

        if user is not None:
            if user.is_active:
                register_login(request, user)
                return redirect('dashboard', user.pk)
            else:
                messages.error(request, 'El usuario no esta activo')
        else:
            messages.error(request, 'usuario y/o contraseña no coinciden')
    else:
        print(login_form.errors)

    data = {'login_form': login_form}
    return TemplateResponse(request, 'login/login.html', data)