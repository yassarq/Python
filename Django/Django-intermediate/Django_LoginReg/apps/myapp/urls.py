from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^success$', views.success),
    url(r'^clear$', views.clear),
    url(r'^logout$', views.logout),
    url(r'^shoes$', views.shoes),
    url(r'^buy/(?P<sale_id>\d+)$', views.buy),
    url(r'^remove/(?P<product_id>\d+)$', views.remove)
]
