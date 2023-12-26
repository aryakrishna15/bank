from . import views
from django.urls import path

app_name = 'bankapp'

urlpatterns = [
     path('', views.home,name='home'),
     path('login/', views.login,name='login'),
     path('register/', views.register,name='register'),
     path('register_form/',views.register_form,name='register_form'),
     path('submit_form/',views.submit_form,name='submit_form'),
     path('logout/',views.logout,name='logout'),
     path('success_page/',views.success_page,name='success_page'),

]

