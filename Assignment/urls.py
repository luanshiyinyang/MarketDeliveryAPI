from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from MyAPI import views
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

# 创建路由器并注册我们的视图。
router = DefaultRouter()
router.register(r'users', views.UserViewSet, base_name="users")
router.register(r'orders', views.OrderViewSet, base_name="orders")
router.register(r'merchants', views.MerchantViewSet, base_name="merchants")
router.register(r'goods', views.GoodViewSet, base_name="goods")

urlpatterns = [
    path('admin/', admin.site.urls),
    # API路由
    path(r'doc', include_docs_urls(title="周晨的说明文档")),
    url(r'^api/', include(router.urls))
]
