from django.conf.urls import url, patterns
from .views import ChatInviteView
from django.contrib import admin

# urlpatterns = [
#     # url(r'^$',  views.about, name='about'),
#     url(r'^new/$', views.new_room, name='new_room'),
#     url(r'^(?P<label>[\w-]{0,50})/$', views.chat_room, name='chat_room'),
# ]

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^invite/$', ChatInviteView.as_view()),
                       )