from django.conf.urls import include, url
from django.contrib import admin
from pansy.views import authentication
from pansy.views.home import HomeView
from django.conf.urls.static import static
from fancy.settings import STATIC_ROOT, STATIC_URL

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signin/', authentication.signin),
    url(r'^signup/', authentication.signup),
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
