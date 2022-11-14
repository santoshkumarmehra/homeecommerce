
from django.contrib import admin
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index.as_view(), name="home"),
    path('home/', views.index.as_view(), name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.Login, name="login"),


    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
