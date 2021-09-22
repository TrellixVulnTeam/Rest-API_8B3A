from django.urls import path, include
from App1 import views

urlpatterns = [
    path('', views.Detail_View.as_view()),
    path('app1/<int:pk>/', views.Update_View.as_view()),
    path('mixin/', views.CarList.as_view()),
    path('accounts/profile/', views.CarCreate.as_view()),
    path('generics_details/<int:pk>/', views.CarDetail.as_view()),
    path('u/<int:pk>/', views.UserList.as_view())
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
