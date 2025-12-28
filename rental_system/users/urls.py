from django.urls import path
from .views import signup,login,verify_email,resend_verification_email

app_name ='accs'

urlpatterns = [
    path('signup/',signup,name='signup'),
    path('login/', login, name='login'),
     path('verify-email/<str:token>/', verify_email, name='verify-email'),
      path('resend-verification-email/', resend_verification_email, name='resend-verification-email'),
]