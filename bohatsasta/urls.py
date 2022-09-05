from django.urls import path,include
from rest_framework import routers
from bohatsasta import views
from rest_framework.authtoken import views as rest_views

#dfdff
router = routers.DefaultRouter()
router.register(r'flights', views.FlightView, 'flights')
# router.register(r'users',views.userView,'users')
router.register(r'detail',views.DetailView,'detail')
# router.register(r'card',views.CardView,'card')
urlpatterns = [
    path('api/',include(router.urls)),
    path('card/', views.CardList.as_view() ,name = 'card'),
    path('card/<int:pk>/',views.CardCRUD.as_view(),name='card'),
    path('token/',rest_views.obtain_auth_token,name='api-token-auth'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('register/',views.RegisterUserAPIView.as_view(), name='register'),
    path('user/',views.UserDetailAPI.as_view(),name='user'),
    path('ticket/',views.TicketView.as_view(),name = 'ticket'),
]
