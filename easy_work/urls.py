from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from candidates.views import CandidateViewSet, EducationViewSet, CertificateViewSet, SiteViewSet, ExperienceViewSet
from django.urls import include



router = SimpleRouter()
router.register('candidates', CandidateViewSet)
router.register(r'candidates/(?P<candidate_id>\d+)/educations', EducationViewSet, basename='education')
router.register(r'candidates/(?P<candidate_id>\d+)/certificates', CertificateViewSet, basename='certificate')
router.register(r'candidates/(?P<candidate_id>\d+)/sites', SiteViewSet, basename='site')
router.register(r'candidates/(?P<candidate_id>\d+)/experiences', ExperienceViewSet, basename='experience')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
