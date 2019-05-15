from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.MrtList.as_view(), name='mrt_list'),
    path('new', views.MrtCreate.as_view(), name='mrt_new'),
    path('edit/<int:pk>', views.MrtUpdate.as_view(), name='mrt_edit'),
    path('delete/<int:pk>', views.MrtDelete.as_view(), name='mrt_delete'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    
]
