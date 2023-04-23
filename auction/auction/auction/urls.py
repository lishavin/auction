from django.contrib import admin
from django.urls import path
from auction_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('detail/<int:items_id>/', views.detail, name='detail'),
    path('add_item.html/', views.add_item, name='add_item'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#static(settings.STATIC_URL, document_root = settings.STATIC_ROOT),
