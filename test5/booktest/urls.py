from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^uploadPic/$',views.uploadPic),
    url(r'^uploadHandel/$',views.uploadHandel),
    url(r'^herolist/(\d*)/&',views.herolist),
    url(r'^area/$',views.area),
    url(r'^area/(\d+)/$',views.area2)
]