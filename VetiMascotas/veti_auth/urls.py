from django.urls import path
from .views import Login, Register
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/',Register, name='register'),
    path('login/',Login, name='login'),
	path('logout/', LogoutView.as_view(template_name='logout.html'),name='logout')
]
