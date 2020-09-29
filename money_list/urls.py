from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'money_list'

urlpatterns = [
    url(r'^$', views.money_list.as_view(), name='money_list'),
    url(r'^insert/$', views.check_post, name='money_list_insert'),
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

