from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('contact/', views.contact, name='contact'),
    path('certificates/', views.all_certificates, name='certificates'),
    path('skills/', views.all_skills, name='skills'),
    path('projects/', views.all_projects, name='projects'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
