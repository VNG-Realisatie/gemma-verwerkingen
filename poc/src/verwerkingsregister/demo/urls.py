from django.urls import path

from . import views

app_name = 'demo'
urlpatterns = [
    path('<int:pk>/preview/', views.VergunningsAanvraagPreview.as_view(), name='preview'),
    path('<int:pk>/detail/', views.VergunningsAanvraagUpdate.as_view(), name='update'),
    path('', views.VergunningsAanvraagList.as_view(), name='list'),
]
