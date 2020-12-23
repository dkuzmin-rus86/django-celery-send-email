from django.urls import path
# from django.conf.urls import url

from send_email_app.models import Post
from send_email_app.views import (
    PostDetailView, 
    home, 
    verify
)


urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('verify/<uuid:uuid>/', verify, name='verify'),

]
