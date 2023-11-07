"""
URL configuration for Agit_Company_Inner_Website project.

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
from django.contrib import admin
from django.urls import path
from index.views import homepage
from about.views import aboutView
from fastlink.views import fastlinkView
from award.views import awardView
from blog.views import blogView, blog_single_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', homepage, name='index'),
                  path('about/', aboutView, name='about'),
                  path('fastlink/', fastlinkView, name='fastlink'),
                  path('awarad/', awardView, name='award'),
                  path('blog-sidebar/', blogView, name='blog-sidebar'),
                  path('blog-single/<int:article_id>', blog_single_view, name='blog-single'),
                  path('admin/', admin.site.urls),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
