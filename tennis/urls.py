
from booking import views
from django.contrib.auth import views as auth_views
from booking import views as booking_views
from django.urls import path, include
from django.contrib import admin
# URL configuration for tennis project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https: // docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
# 1. Add an import: from my_app import views
# 2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
# 1. Add an import: from other_app.views import Home
# 2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
# 1. Import the include() function: from django.urls import include, path
# 2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


urlpatterns = [
    path('', booking_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('booking/', include('booking.urls')),  # app URLs
    path('login/', booking_views.CustomLoginView.as_view(),
         name='login'),  # custom login with message
    path('logout/', booking_views.logout_view,
         name='logout'),  # logout with message
    path('register/', booking_views.register, name='register'),  # registration
]
