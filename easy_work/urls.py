from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from candidates.views import CandidateViewSet
from django.urls import include
router = SimpleRouter()
router.register('candidate', CandidateViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
