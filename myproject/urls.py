from tkinter.font import names

from django.contrib import admin
from django.urls import path, include
from pages.views import admin_only_page
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('admin-only/', admin_only_page, name='admin_only'),
    path('pageCSS/', views.page1, name='pageCSS'),
    path('bootstrap/', views.bootstrap_template, name='bootstrap_template'),

]
