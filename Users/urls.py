# from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.HomePage, name="homepage"),
    url(r'^register/', views.Register, name="register"),
    url(r'^login/', views.LoginSubmit, name="login"),
    url(r'^logout/', views.logout_user, name="logout"),
    url(r'^home/', views.home, name="home")
]