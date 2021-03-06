from django.contrib import admin
from django.urls import include, re_path
from .import views
from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^articles/', include('articles.urls')),
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^about/$', views.about),
    re_path(r'^$', article_views.article_list, name="home"),

    # path(r'^admin/', admin.site.urls),
    # path(r'^about/$', views.about),
    # path(r'^$', views.homepage)
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
