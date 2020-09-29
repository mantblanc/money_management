from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'money_main'

urlpatterns = [
    url(r'^$', views.money_main.as_view(), name='money_main'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


