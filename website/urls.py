from django.urls import path, include
from Inventory.settings import settings

from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
                  path('', views.IndexView.as_view(), name='website.index'),
                  path('event/', views.EventView.as_view(), name='website.event'),
                  path('add_event/', TemplateView.as_view(template_name='add_event.html'), name='website.add_event'),
                  path('accounts/', include('django.contrib.auth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
