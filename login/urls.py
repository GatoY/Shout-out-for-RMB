from django.conf.urls import url
from . import views

app_name = 'login'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^infoForm/$',views.infoForm, name = 'infoForm'),
    url(r'^result/$', views.result, name = 'result'),
    url(r'^register/home/$',views.result, name='home'),
    
]
