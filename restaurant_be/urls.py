from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from restaurant import views
from restaurant.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')), #allow login/logout for non-admin from local server page
    path('api/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.food_menu),
    path('api/menu/', views.food_menu),
    path('api/menu/<int:pk>', views.getMenu),
    path('register/', RegisterView.as_view(), name='auth_register'),
]