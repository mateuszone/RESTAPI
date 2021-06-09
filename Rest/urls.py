from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from Api import urls
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
    path('auth/', obtain_auth_token)
    # path('v2/', include(urls)),
]

urlpatterns += [

]