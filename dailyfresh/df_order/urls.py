from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.order),
    url(r'^suborder/$',views.suborder),
    # url(r'^addorder/$',views.addorder),
]