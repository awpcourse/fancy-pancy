from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from fancy.settings import STATIC_ROOT, STATIC_URL, MEDIA_ROOT, MEDIA_URL
from pansy.views import authentication
from pansy.views.photo import PhotoView, AddPhotoView
from pansy.views.home import HomeView
from pansy.views.search import search_view

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^photo/(?P<pk>\d+)/$', PhotoView.as_view(), name='photo'),
    url(r'^add-photo/', AddPhotoView.as_view(), name='add-photo'),
    # url(r'^photos/', PhotoView.as_view(), name='photos'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signin/', authentication.signin, name="signin"),
    url(r'^signup/', authentication.signup, name="signup"),
    url(r'^signout/', authentication.signout, name="signout"),
    url(r'^search/', search_view, name="search")
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
