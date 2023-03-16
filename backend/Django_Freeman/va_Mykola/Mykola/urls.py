from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from va_Mykola import settings
from .views import *

# HomePage/ - Search link. In example: 127.0.0.1:8000/HomePage, homepage - views page.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('HomePage/', home_page, name='home'),
    path('HelpPage/', help_page, name='help'),
    path('Register/', register_page, name='register'),
    path('MykolasHouse/<int:page_num>/', num_home),
    path('api/v1/users/', MykolaAPIView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
