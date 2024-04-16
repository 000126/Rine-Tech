from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponseNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rineapp.urls')),
    path('auth/', include('authentication.urls')),
    path('favicon.ico', lambda x: HttpResponseNotFound())

    # path(r'^api/password_reset/',
    #      include('django_rest_passwordreset.urls', namespace='password_reset')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
