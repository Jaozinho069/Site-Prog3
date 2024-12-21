from django.contrib import admin
from django.urls import path
from sites.views import home
from django.conf import settings
from django.conf.urls.static import static
from sites import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('atividades/', views.atividades, name='atividades'),  
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('cadusuario/', views.cadusuario_view, name='cadusuario'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
