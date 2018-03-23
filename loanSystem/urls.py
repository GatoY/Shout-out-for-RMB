from django.conf.urls import include, url
from django.contrib import admin
from login import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',include('login.urls',namespace='login')),
    url(r'^login/',include('django.contrib.auth.urls')),
    url(r'^$',views.index,name='index'),
    url(r'^accounts/profile/$',views.home, name = 'home'),
    url(r'^infoForm',views.infoForm, name = 'info'),
    url(r'^result',views.result, name='result'),
]
