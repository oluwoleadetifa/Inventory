from django.urls import path
from Inventory.settings import settings

from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('', views.IndexView.as_view(), name='website.index')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
