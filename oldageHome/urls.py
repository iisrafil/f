"""oldageHome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.views import auth_login, logout_view
from dashboard.views import dashboard_home, oldage_home, patient_list, illness_list, add_oldage_home, \
    update_oldage_home, doctors_list, oldage_home_details, oldage_home_members, oldage_home_doctors, oldage_home_patient
from landing.views import landing_home
from oldageHome import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_home, name='landing_home'),
    path("login/", auth_login, name='login'),
    path("logout/", logout_view, name='logout'),
    path('dashboard/', dashboard_home, name='dashboard_home'),
    path('dashboard/home/', dashboard_home, name='dashboard_home'),
    path('dashboard/oldagehomes/', oldage_home, name='oldage_home'),
    path('dashboard/oldagehomes/<pk>', oldage_home_details, name='oldage_home_details'),
    path('dashboard/oldagehomes/members/<pk>', oldage_home_members, name='oldage_home_members'),
    path('dashboard/oldagehomes/doctors/<pk>', oldage_home_doctors, name='oldage_home_doctors'),
    path('dashboard/oldagehomes/patient/<pk>', oldage_home_patient, name='oldage_home_patient'),
    path('dashboard/oldagehomes/add/', add_oldage_home, name='add_oldage_home'),
    path('dashboard/oldagehomes/update/<pk>)', update_oldage_home, name='update_oldage_home'),
    path('dashboard/patient-list/', patient_list, name='Patient_list'),
    path('dashboard/ill-patient-list/', illness_list, name='illness_list'),
    path('dashboard/doctors-list/', doctors_list, name='doctors_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
