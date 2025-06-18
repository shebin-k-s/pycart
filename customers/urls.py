from django.urls import path

from . import views


urlpatterns = [
    path('',views.account_view,name='account'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout_user,name='logout'),
]