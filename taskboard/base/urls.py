from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet, AdminViewSet, home , RssView

from django.urls import path
from .feeds import LatestEntriesFeed

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)
router.register(r'admins', AdminViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
    
    path("latest/feed/", LatestEntriesFeed()),
    path('Task/<int:pk>/', LatestEntriesFeed(), name='news-item'),
    path('rss/', RssView, name='rss'),
]
