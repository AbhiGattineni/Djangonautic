from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('about/', views.about),

    # path(r'^admin/', admin.site.urls),
    # path(r'^about/$', views.about),
    # path(r'^$', views.homepage)
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
