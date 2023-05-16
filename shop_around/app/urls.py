from django.conf import settings
from .views import *
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('',HomeView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
