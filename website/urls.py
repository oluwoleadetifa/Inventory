from django.urls import path, include
from Inventory.settings import settings

from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

app_name = "website"

urlpatterns = [
                  path('', views.IndexView, name='website.index'),
                  path('logout/', views.logoutUser, name='website.logout'),
                  path('event/', views.EventView.as_view(), name='website.event'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
