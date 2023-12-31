from django.urls import path
from . import views
from django.conf import settings
from .views import Logout

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('logout', Logout.as_view(), name='logout')
]