from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('inscription', views.register, name='inscription'),
    path('connexion/', LoginView.as_view(template_name = 'EspacePerso/connexion.html', redirect_field_name = 'index.html'),  name = 'login'),
    path('deconnexion/', LogoutView.as_view(template_name = 'EspacePerso/deconnecte.html'), name = 'logout'),
    path('connect', views.connect, name = 'connect'),
    path('', views.personal_space, name = 'personal_space'),
]    