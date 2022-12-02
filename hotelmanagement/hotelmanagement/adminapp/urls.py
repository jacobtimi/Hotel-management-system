from django.conf.urls import url
from django.contrib.staticfiles.urls import urlpatterns
from hotelmanagement.adminapp import views as admin_view

urlpatterns = [
url(r'^manage_staff/$', admin_view.manage_staff, name='manage_staff'),
url(r'^manage_customer/$', admin_view.manage_customer, name='manage_customer'),
url(r'^staff_profile/(?P<user_id>\d+)/', admin_view.staff_profile, name='staff_profile'),
url(r'^edit_profile/(?P<user_id>\d+)/', admin_view.edit_profile, name='edit_profile'),
url(r'^user_profile/(?P<user_id>\d+)/', admin_view.staff_profile, name='user_profile'),
url(r'^staff_deactivate/(?P<user_id>\d+)/', admin_view.staff_deactivate, name='staff_deactivate'),
url(r'^room_upload/', admin_view.upload_room, name='upload_room'),
url(r'^manage_room/$', admin_view.manage_room, name='manage_room'),
url(r'^room_status/(?P<prod_id>\d+)/', admin_view.approve_Room,name='status_room'),
url(r'^edit_room/(?P<prod_id>\d+)/', admin_view.edit_room, name='edit_room'),
url(r'^delete_room/(?P<prod_id>\d+)/', admin_view.delete_room, name='delete_room'),
]   