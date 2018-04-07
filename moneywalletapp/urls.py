from django.conf.urls import url
from . import views
urlpatterns=[url(r'^$',views.homepage,name='homepage'),
             url(r'^reg$',views.register,name='reg'),
             url(r'^logi$',views.logi,name='logi'),
              url(r'^paynow$',views.paynow,name='paynow'),]

