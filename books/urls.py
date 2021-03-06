from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookItemViewSet

router = DefaultRouter()
router.register("books", BookViewSet)
router.register("books_items", BookItemViewSet)
urlpatterns = router.urls