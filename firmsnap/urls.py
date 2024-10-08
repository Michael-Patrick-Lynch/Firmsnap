"""
URL configuration for firmsnap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.shortcuts import redirect
from django.urls import include, path
from app.views import CustomLoginView, custom_error_view


urlpatterns = [
    path('', lambda request: redirect('all_posts', permanent=True)),  # Redirect root URL to 'all_posts' URL pattern
    path("app/", include("app.urls")),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")), # django_tailwind

    # Need a custom login view because I want to redirect users to 
    # their feed when they login (as opposed to their profile)
    path('accounts/login/', CustomLoginView.as_view(), name='login'),

    # This provides the following URL patterns:
    # accounts/login/ [name='login']
    # accounts/logout/ [name='logout']
    # accounts/password_change/ [name='password_change']
    # accounts/password_change/done/ [name='password_change_done']
    # accounts/password_reset/ [name='password_reset']
    # accounts/password_reset/done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']
    path("accounts/", include("django.contrib.auth.urls")),
]

def handler404(request, exception):
    return custom_error_view(request, status_code=404, message='Page Not Found')

def handler500(request):
    return custom_error_view(request, status_code=500, message='Internal Server Error')

def handler403(request, exception):
    return custom_error_view(request, status_code=403, message='Access Denied')

def handler400(request, exception):
    return custom_error_view(request, status_code=400, message='Bad Request')

handler400 = handler400
handler403 = handler403
handler404 = handler404
handler500 = handler500
