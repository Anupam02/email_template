from django.conf.urls import url 
from .import views

urlpatterns = [
    url('^$',views.index, name='index'),
    url('email_hubbler', views.emailsent, name='emailsent'),
    # url(r'^details/(?P<id>\d+)/$', views.details, name='details')

];