from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^logs/', include('Logs.urls')),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    url(r'', include('Users.urls')),
]

