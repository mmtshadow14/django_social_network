from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('postDetail/<int:pk>', views.PostDetailView.as_view(), name='postDetail'),
    path('profile/<int:user_id>', views.ProfileView.as_view(), name='profile'),
]