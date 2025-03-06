from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from accounts.api import (
    UserViewSet,
    UserSearchView,
    AvatarViewSet,
    GuestRegistration,
    AuthSetup,
)
from boards.api import (
    BoardViewSet,
    ColumnViewSet,
    LabelViewSet,
    TaskViewSet,
    SortColumn,
    SortTask,
    CommentViewSet,
)

# Initialize router
router = routers.DefaultRouter()
router.register(r"avatars", AvatarViewSet)
router.register(r"users", UserViewSet)
router.register(r"boards", BoardViewSet)
router.register(r"columns", ColumnViewSet)
router.register(r"labels", LabelViewSet)
router.register(r"tasks", TaskViewSet)
router.register(r"comments", CommentViewSet)

# Set up Swagger view
schema_view = get_schema_view(
    openapi.Info(
        title="KanBan API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@kanban.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL patterns
urlpatterns = [
    path("api/", include(router.urls)),
    path("api/u/search/", UserSearchView.as_view(), name="user-search"),
    path("api/sort/column/", SortColumn.as_view(), name="sort-column"),
    path("api/sort/task/", SortTask.as_view(), name="sort-task"),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    path("auth/setup/", AuthSetup.as_view(), name="auth-setup"),
    path("auth/guest/", GuestRegistration.as_view(), name="guest-registration"),
    path("backdoor/", admin.site.urls),
    
    # Add Swagger URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),  # Swagger UI URL
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    try:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
    except ModuleNotFoundError:
        pass
