from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import ArticleViewSet


# urlpatterns = [
#     path('', ArticleListView.as_view()),
#     path('create/', ArticleCreateView.as_view()),
#     path('<pk>', ArticleDetailView.as_view()),
#     path('<pk>/update/', ArticleUpdateView.as_view()),
#     path('<pk>/delete/', ArticleDeleteView.as_view()),

# ]


router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='user')
urlpatterns = router.urls
