from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from users.views.base import logout_user, login_redirect, LoginUserView, IndexTemplateView


urlpatterns = [
    # path('', IndexTemplateView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('accounts/',include('allauth.urls')),
    path('accounts/logout', logout_user, name='logout'),
    # path('', LoginUserView.as_view(template_name='account/login.html'), name='login'),
    path('', LoginView.as_view(template_name='account/login.html'),name='login'),
    path('accounts/login-redirect/', login_redirect, name='login_redirect'),
    path('dashboard/',include('dashboard.urls',namespace='dashboard')),
    path('users/',include('users.urls',namespace='users')),
    path('schools/',include('schools.urls',namespace='schools')),
    path('equipment/',include('equipment.urls',namespace='equipment')),

]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
