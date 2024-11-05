from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.urls import path
from .forms import LoginForm

app_name="myapp"

urlpatterns = [
    path('', views.home, name='index'),
    path('dm/', views.disaster_management, name='dm'),
    path('medical/', views.medical, name='medical'),
    path('signup/',views.signup,name="signup"),
    path("login/",auth_views.LoginView.as_view(template_name="myapp/login.html",authentication_form=LoginForm),name="login"),
    path("logout/",views.logout_view,name="logout"),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('send_sms/',views.send_sms,name='send_sms'),
    path('medical_purpose/', views.medical_purpose_view, name='medical_purpose'),
    path('food_purpose/', views.food_purpose_view, name='food_purpose'),
    path('immediate/', views.immediate_purpose_view, name='immediate'),
    path('medical-purpose-list/', views.medical_purpose_list_view, name='medical_purpose_list'),
    path('food-purpose-list/', views.food_purpose_list_view, name='food_purpose_list'),
    path('immediate-purpose-list/', views.immediate_purpose_list_view, name='immediate_purpose_list'),
    path('failmsg/', views.failmsg_list_view, name='failmsg' )
  

]
