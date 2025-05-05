"""
URL configuration for Environment_sustainability project.

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
from userapp import views as userviews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',userviews.index,name="index"),
    path('user/about/',userviews.about,name="about"),
    path('user/userRegister/',userviews.userRegister,name="userRegister"),
    path('user/user-login/',userviews.userLogin,name="userLogin"),
    path('user/user-register/',userviews.userRegister,name="userRegister"),
    path('user/contact/',userviews.contact,name="contact"),
    path('user/dashboard/',userviews.userDashboard,name="userDashboard"),
    path('user/prediction/',userviews.Classification,name="prediction"),
    path('user/feedback/',userviews.feedback,name="feedback"),
    path('user/chatbot/',userviews.chatbot,name="chatbot"),
    path('user/myprofile/',userviews.myprofile,name="myprofile"),
    path('user/result/',userviews.Classification_result,name="result"),
    path('user/otp/',userviews.otp,name="otp"),
    path('logout/',userviews.user_logout,name="log_out"),









]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)