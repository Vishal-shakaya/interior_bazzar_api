
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from app_ib import views
from rest_framework_simplejwt.views import (TokenRefreshView)
from app_ib.Views import AuthView, BusinessView, QueryView, Feedback
from app_ib.Views import ProfileView


app_name = 'interior_bazzar'
urlpatterns = [
    #########################################################
    # Test: 
    #########################################################
    path('test', views.TestView, name='TestView'),
    path('test-mail', views.TestMailView, name='TestMailView'),
    #########################################################
    # Authentication: 
    #########################################################
    path('v-1/signup', AuthView.SignupView, name='SignupView'),
    path('v-1/login', AuthView.LoginView, name='LoginView'),
    path('v-1/logout', AuthView.LogoutView, name='LogoutView'),
    path('v-1/delete-account', AuthView.DeleteAccountView, name='DeleteAccountView'),  
    path('v-1/forgot_password_request', AuthView.ForgotPasswordRequestView, name='ForgotPasswordRequestView'),
    path('v-1/forgot-password/<str:hash>', AuthView.ForgotPasswordView, name='ForgotPasswordView'),
    path('v-1/change-password', AuthView.ChnagePasswordView, name='ChnagePasswordView'),
    path('v-1/reset-password', AuthView.ResetPasswordView, name='ResetPasswordView'),
    
    #########################################################
    # Tokem: 
    #########################################################
    path('v-1/get-refresh-token', TokenRefreshView.as_view(), name='token-refresh'),

    #########################################################
    # User Profile: 
    #########################################################
    path('v-1/create-profile', ProfileView.CreateProfileView, name='CreateProfileView'),
    path('v-1/create-update-profile-image', ProfileView.CreateOrUpdateProfileImageView, name='CreateOrUpdateProfileImageView'),
    path('v-1/get-profile', ProfileView.GetProfileView, name='GetProfileView'),



    #########################################################
    # Business: 
    #########################################################
    path('v-1/create-business', BusinessView.CreateBusinessView, name='CreateBusinessView'),
    path('v-1/update-business', BusinessView.UpdateBusinessView, name='UpdateBusinessView'),
    path('v-1/get-business-by-id/<int:id>', BusinessView.GetBusinessByIdView, name='GetBusinessByIdView'),
    path('v-1/get-all-business', BusinessView.GetAllBusinessView, name='GetAllBusinessView'),
    #########################################################
    # Query: 
    #########################################################
    path('v-1/create-query', QueryView.CreateQueryView, name='CreateQueryView'),
    path('v-1/get-query-by-id/<int:id>', QueryView.GetQueryByIdView, name='GetQueryByIdView'),
    path('v-1/get-query-by-business-id/<int:id>', QueryView.GetQueryBusinessIdView, name='GetQueryBusinessIdView'),
  
    #########################################################
    # Feedback: 
    #########################################################
    path('v-1/create-feedback', Feedback.CreateFeedbackView, name='CreateFeedbackView'),
]
