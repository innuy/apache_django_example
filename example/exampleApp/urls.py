from django.conf.urls import url
from exampleApp.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name= "index"),

]