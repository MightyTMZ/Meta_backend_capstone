from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r"tables", views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name="menu-list-create"),
    path('menu/<int:pk>', views.SingleMenuItemVIew.as_view(), name="menu-detail"),
    path("LittleLemonAPI/booking/", include(router.urls)),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]
