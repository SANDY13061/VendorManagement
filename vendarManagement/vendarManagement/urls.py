"""
URL configuration for vendarManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vendors.views import VendorListCreateAPIView, VendorRetrieveUpdateDestroyAPIView, vendor_performance,RegisterToken
from purchaseOrders.views import PurchaseOrderListCreateAPIView, PurchaseOrderRetrieveUpdateDestroyAPIView, acknowledge_purchase_order
from rest_framework.authtoken import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-retrieve-update-destroy'),
    path('api/vendors/<int:vendor_id>/performance/', vendor_performance, name='vendor-performance'),
    path('api/vendors/', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('api/get-auth-token/', views.obtain_auth_token, name='get_auth_token'),
    path('api/register-token/', RegisterToken.as_view(), name='register_token'),
    path('api/purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='create-purchase-order'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchase_order_detail'),
    path('api/purchase_orders/<int:po_id>/acknowledge/', acknowledge_purchase_order, name='acknowledge-purchase-order'),
]