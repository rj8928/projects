from django.conf.urls import url
import views

urlpatterns = [
    url(r'^register/$',views.register),
    url(r'^register_handle/$',views.register_handle),
    url(r'^check_user(\w+)/$',views.check_user),
    url(r'^login/$',views.login),
    url(r'^login_handle/$',views.login_handle),
    url(r'^info/$',views.usercenterinfo),
    url(r'^order/$',views.usercenterorder),
    url(r'^site/$',views.usercentersite),
    url(r'^editorinfo/$',views.editorinfo),
]