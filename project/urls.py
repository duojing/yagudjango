from django.conf.urls import url
from project import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.gujang_list, name = 'gujang_list'),
    url(r'^(?P<id>\d+)/$' , views.gujang_detail, name= 'gujang_detail'),
    url(r'^main/$' , views.gujang_main)
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)