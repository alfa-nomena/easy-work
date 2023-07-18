from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from candidates.views import CandidateViewSet, EducationViewSet, CertificateViewSet, SiteCandidateViewSet, ExperienceViewSet
from enterprises.views import EnterpriseViewSet, SiteEnterpriseViewSet
from jobs.views import JobViewset
from django.urls import include



router = SimpleRouter()
router.register(r'^candidates', CandidateViewSet)
router.register(r'^candidates/(?P<candidate_id>\d+)/educations', EducationViewSet, basename='education')
router.register(r'^candidates/(?P<candidate_id>\d+)/certificates', CertificateViewSet, basename='certificate')
router.register(r'^candidates/(?P<candidate_id>\d+)/sites', SiteCandidateViewSet, basename='site_candidate')
router.register(r'^candidates/(?P<candidate_id>\d+)/experiences', ExperienceViewSet, basename='experience')
router.register(r'^enterprises', EnterpriseViewSet, basename='enterprise')
router.register(r'^enterprises/(?P<enterprise_id>\d+)/sites', SiteEnterpriseViewSet, basename='site_enterprise')
router.register(r'^enterprises/(?P<enterprise_id>\d+)/jobs', JobViewset, basename='job_enterprise')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
