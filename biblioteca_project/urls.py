"""
URL configuration for biblioteca_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# biblioteca_project/urls.py

from django.contrib import admin
from django.urls import path, include
from libros import web_views
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. ESTA LÍNEA ES VITAL: Activa todas las rutas de Google
    path('accounts/', include('allauth.urls')), 
    
    # 2. Rutas de tu API
    path('api/', include('libros.api_urls')),
    
    # 3. Tus vistas de prueba
    path('', web_views.home, name='home'),
    path('oauth/login/', web_views.oauth_login, name='oauth_login'),
    path('login/jwt/', web_views.jwt_login_page, name='jwt_login_page'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]