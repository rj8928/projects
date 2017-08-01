from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^list/(?P<id>\d+)/(?P<sort>\d+)/(?P<Pindex>\d*)$',views.list),
    url(r'^detail/(\d+)/$',views.detail),

]