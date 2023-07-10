
from django.contrib import admin
from django.urls import path, include
# from oauth2_provider import views as oauth2_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cliente.urls')),
    # path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]
