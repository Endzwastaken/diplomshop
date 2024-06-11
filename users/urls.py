from django.urls import path
from users import views as users

app_name = 'users'

urlpatterns = [
    path('login/', users.login, name='login'),
    path('registration/', users.registration, name='registration'),
    path('profile/', users.profile, name='profile'),
    path('logout/', users.logout, name='logout'),

]