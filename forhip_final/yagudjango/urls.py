from django.conf.urls import url
from yagudjango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.gujang_list, name ='gujang_list'),
    url(r'^(?P<pk>\d+)/$', views.gujang_detail, name='gujang_detail'),
    url(r'^(?P<pk>\d+)/yet/$', views.gujang_detail_yet, name='gujang_detail_yet'),
    url(r'^(?P<pk>\d+)/(?P<block_name>\d+)/$', views.block_detail, name='block_detail'),


    # url(r'^block/$', views.index, name='index'),
    # url(r'^blocks/(?P<pk>\d+)/$', views.block_detail, name='block_detail'),
    # url(r'^(?P<post_pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),
    # url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    # url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/delete/$',views.comment_delete, name='comment_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)