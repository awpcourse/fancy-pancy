from django.conf.urls import include, url
from django.contrib import admin
<<<<<<< HEAD
from pansy.views import authentication
=======
from pansy.views.home import HomeView
>>>>>>> 29ac17e5f44de35534b9d7c6540b7edebe114f8b

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signin/', authentication.signin),
    url(r'^signup/', authentication.signup),
]
