from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("app.user_app.urls")),
]
