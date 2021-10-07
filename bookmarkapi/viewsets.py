from rest_framework import viewsets
from . import models
from . import serializers

class BookmarkViewset(viewsets.ModelViewSet):
    queryset = models.Bookmark.objects.all()
    serializer_class = serializers.BookmarkSerializer