from django.urls import path
from .views import import_google_drive, list_images

urlpatterns = [
    path('import/google-drive', import_google_drive),
    path('images', list_images),
]
