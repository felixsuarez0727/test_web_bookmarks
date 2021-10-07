from bookmarkapi.viewsets import BookmarkViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('bookmark', BookmarkViewset, basename='BookMark')