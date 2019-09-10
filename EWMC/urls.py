"""EWMC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from EWMC import settings
from . import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index, name='index'),
                  path('nat-test', views.applicationForm, name='applicationForm'),
                  path('sign-in', views.signin, name='signin'),
                  path('Dashboard', views.dashboard, name='dashboard'),
                  path('confirm/<int:id>', views.confirm, name='confirm'),
                  path('logout', views.my_logout, name='logout'),
                  path('Dashboard/Details/<int:id>', views.details, name='details'),
    path('Dashboard/Edit/<int:id>', views.nattest_edit, name='nattest_edit'),
    path('Dashboard/Delete/<int:id>', views.nattest_delete, name='nattest_delete')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
