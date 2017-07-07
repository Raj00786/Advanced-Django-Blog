from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin
from accounts.views import (login_view,logout_view,register_view,forgot_view)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',login_view,name="login"),
    url(r'^logout/$',logout_view,name="logout"),
    url(r'^register/$',register_view,name="register"),
    url(r'^forgot/$',forgot_view,name="forgot"),
    url(r'^api/', include('api.urls')),
    url(r'^',include('blogs.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

