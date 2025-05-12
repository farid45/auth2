from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView 

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),  # Главная страница
    path('oauth/', include('oauthapp.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]

