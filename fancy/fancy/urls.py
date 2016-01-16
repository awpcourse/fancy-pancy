from django.conf.urls import include, url
from django.contrib import admin
from pansy.views.home import HomeView

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^admin/', include(admin.site.urls)),
]
