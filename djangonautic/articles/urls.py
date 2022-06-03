
from django.urls import path
from .import views

urlpatterns = [
    path('', views.article_list),

    # path(r'^admin/', admin.site.urls),
    # path(r'^about/$', views.about),
    # path(r'^$', views.homepage)
]
