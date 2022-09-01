from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView,SpectacularAPIView
from . import views



urlpatterns = [
    path('musicians/', views.MusicianView.as_view()),
    path('musicians/<int:musician_id>/', views.MusicianDetailView.as_view()),
    path('musicians/<int:musician_id>/albums/', views.MusicianAlbumView.as_view()),
    path('musicians/<str:musician_id>/albums/<str:album_pk>/songs/', views.MusicianAlbumSongView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
