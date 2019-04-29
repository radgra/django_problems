from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('grades/',views.GradeList.as_view(),name='grade_list'),
    path('grades/<int:pk>/',views.GradeDetail.as_view(),name='grade_detail'),
    path('api-token-auth/',obtain_auth_token, name='api_token_auth')
]