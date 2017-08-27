from django.conf.urls import url, include
from . import views
from .views import Bot

urlpatterns = [url(r'^4cf1d3c2848cdb26f1c558e8e4/?$', Bot.as_view())]