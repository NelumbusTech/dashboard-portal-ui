from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^v1/users$',views.user_create_and_retreive),
    url(r'^v1/users/active$',views.get_active_users),
    url(r'^v1/users/(?P<email_id>[\S+@\S+]+)$',views.user_update_and_fetch),

]


