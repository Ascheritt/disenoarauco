from django.conf.urls import url
from .views import *


from django.urls import path
from .import views
#from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('index/', home, name='index'),
    
    #Login URL
    #path('index/', LoginF, name='login'),
    #path('index/', auth_views.LoginView.as_view(template_name='arauco/index.html'), name='login'),
    #path('login/', auth_views.LogoutView.as_view(template_name='arauco/login.html'), name='desconectar'),
    #path('index/', auth_views.LoginViews.as_view(template_name='arauco/index.html'), name='indexr'), en proceso
    #Grafico URL
    #path('grafico/', login_required(graficoview), name='grafico'),
]