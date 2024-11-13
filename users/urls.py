from django.urls import path
from django.contrib.auth import views as auth_views
from .views import logout_confirm, logout_done


urlpatterns = [
    path("login/",auth_views.LoginView.as_view(template_name = 'users/login.html'), name= 'login'),
    path("logout/",logout_confirm, name = 'logout-confirm' ),
    path("logout-done/", logout_done, name='logout-done'),
]