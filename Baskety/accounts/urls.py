from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, dashboard

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', CustomLoginView.as_view(), name='home'), # Redirect root to login
]
