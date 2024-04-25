from django.urls import path
from . import views

urlpatterns = [
    
    path('prediction/',views.prediction, name='predict'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('edit/',views.edit, name='edit_info'),
    path('prediction/result', views.result),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('signup/',views.signup, name='signup'),
    path('dashboard/<updated_info>/', views.dashboard, name='dashboard_with_info'),
    
    path('history/',views.history, name='history'),
    path('',views.home),
    
]
 