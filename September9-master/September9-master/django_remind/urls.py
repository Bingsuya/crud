from django.contrib import admin
from django.urls import path, include
from user.views import home
import classcrud.urls
import classcrud.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('', home, name='home'),
    path('classcrud/', include('classcrud.urls')),
]
