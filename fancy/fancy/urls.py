from django.conf.urls import include, url
from django.contrib import admin
from pansy.views.home import HomeView
from pansy.views.photo import PhotoView

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^photo/(?P<pk>\d+)/$', PhotoView.as_view(), name='photo'),
    # url(r'^photos/', PhotoView.as_view(), name='photos'),

    url(r'^admin/', include(admin.site.urls)),
]
