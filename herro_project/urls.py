"""
URL configuration for herro_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from herro.views import *
from accounts.views import *
from herro_project import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index,name="index"),
    path("signup/",signup,name="signup"),
    path("login/",login_user,name="login"),
    path("logout/",logout_user,name="logout"),
    path("add_exercice/",add_exercice,name="add_exercice"),
    path("ajouter_performance/",ajouter_performance,name="ajouter_performance"),
    path("Mes_perfs/",Mes_perfs,name="Mes_perfs"),
    path("search_users",search_users,name="search_users")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

