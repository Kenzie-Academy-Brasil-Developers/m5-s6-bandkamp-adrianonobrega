from albums.models import Album
from albums.serializers import AlbumSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from songs.models import Songs
from songs.serializers import SongsSerializer
from .models import Musician
from .serializers import MusicianSerializer


class MusicianView(generics.CreateAPIView,generics.ListAPIView):
   serializer_class = MusicianSerializer
   queryset = Musician.objects.all()


class MusicianDetailView(generics.RetrieveUpdateDestroyAPIView):
     serializer_class = MusicianSerializer
     queryset = Musician.objects.all()

class MusicianAlbumView(generics.ListCreateAPIView):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()
    
    def perform_create(self, serializer):
        musician_id = self.kwargs["pk"]
        musician = get_object_or_404(Musician, pk=musician_id)

        serializer.save(musician=musician)

    def get_queryset(self):
        musician_id = self.request.path.split("/")[3]
        musician = get_object_or_404(Musician,id = musician_id )

        route_parameter_gt = self.request.GET.get("duration_gt")
        route_parameter_lt = self.request.GET.get("duration_lt")

        if route_parameter_gt:
            queryset = []
            for i in  range(len(musician.albums.all())):
                total_duration = AlbumSerializer(musician.albums.all()[i]).data["total_duration"]
                if total_duration > int(route_parameter_gt): 
                    queryset.append(musician.albums.all()[i])
            return queryset

        route_parameter_lt = self.request.GET.get("duration_lt")

        if route_parameter_lt:
            queryset = []
            for i in  range(len(musician.albums.all())):
                total_duration = AlbumSerializer(musician.albums.all()[i]).data["total_duration"]
                if total_duration < int(route_parameter_lt): 
                    queryset.append(musician.albums.all()[i])
            return queryset    

        
        return musician.albums.all()

class MusicianAlbumSongView(generics.ListCreateAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

    def perform_create(self,serializer):
        musician_id = self.request.path.split("/")[3]
        album_id = self.request.path.split("/")[5]
        album = get_object_or_404(Album,id = album_id)
        get_object_or_404(Musician,id = musician_id )
        serializer.save(album=album)

    def get_queryset(self):
        album_id = self.request.path.split("/")[5]
        album = get_object_or_404(Album,id = album_id)
        return album.songs.all()        