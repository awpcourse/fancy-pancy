from django.conf.urls import include, url
from django.contrib import admin
from pansy.views import authentication

urlpatterns = [
    # Examples:
    # url(r'^$', 'fancy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signin/', authentication.signin),
    url(r'^signup/', authentication.signup),
]
