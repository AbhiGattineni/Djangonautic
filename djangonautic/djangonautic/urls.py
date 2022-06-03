from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('articles/', include('articles.urls')),

    # path(r'^admin/', admin.site.urls),
    # path(r'^about/$', views.about),
    # path(r'^$', views.homepage)
]

urlpatterns += staticfiles_urlpatterns()
