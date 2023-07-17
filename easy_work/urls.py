from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from candidates.views import CandidateViewSet, EducationViewSet, CertificateViewSet
from django.urls import include



router = SimpleRouter()
router.register('candidates', CandidateViewSet)
router.register(r'candidates/(?P<candidate_id>\d+)/educations', EducationViewSet, basename='education')
router.register(r'candidates/(?P<candidate_id>\d+)/certificates', CertificateViewSet, basename='certificate')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
