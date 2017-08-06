from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.cart),
    url(r'(\d+)/(\d+)/$',views.addtocart),
    url(r'^del/(\d+)/$',views.del_cart_goods),
    url(r'^buy_now/$',views.buy_now)
]