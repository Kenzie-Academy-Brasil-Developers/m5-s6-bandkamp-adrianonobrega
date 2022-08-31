from dataclasses import field
from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = "__all__"

    def get_total_duration(self, album: Album):
        songs = album.songs.all()
        total_duration = 0
        for song in songs:
            total_duration += song.duration
        return total_duration    

    def get_songs_count(self, album: Album):
        songs_count = album.songs.all().count()
        return songs_count

    def create(self, validated_data):
        return Album.objects.create(**validated_data)    