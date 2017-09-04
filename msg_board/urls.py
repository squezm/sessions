from django.conf.urls import url
from . import views


app_name = 'msg_board'
urlpatterns = [
    #below url is: [domain]/msg_board/
    url(r'^$', views.MessageBoardIndexView.as_view(), name='message_index'),
    url(r'^logout/', views.LogoutView.as_view(), name='logout'),
    url(r'^error_page/(?P<error>[\w\s\.\,]+)/', views.ErrorView.as_view(), name='error_page'),
    url(r'^vote/', views.Board_pollView.as_view(), name='vote'),
    url(r'^create_account/', views.CreateAccountView.as_view(), name='create_account'),
    url(r'^locations/(?P<location>[\w\_]+)/', views.MsgBoardView.as_view(), name='message_board'),
    url(r'^guest_login/(?P<location>[\w\_]+)', views.GuestLoginView.as_view(), name='guest_login'),
]
