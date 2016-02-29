from django.conf.urls import url
import views

urlpatterns = [
    url(r'token$', views.token, name="token"),
    url(r'$', views.chat, name="chat"),
]