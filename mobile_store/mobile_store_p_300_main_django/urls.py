"""mobile_store_p_300_main_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_header = "ALEcom"
admin.site.site_title = "AL Ecom Panel"
admin.site.index_title = "Welcomee AL Ecom Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_panel.urls')),
    path('admin_panel/', include('admin_panel.urls')),
    path('user_auth/', include('user_auth.urls')),
    path('user_chatbot/', include('user_chatbot.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
