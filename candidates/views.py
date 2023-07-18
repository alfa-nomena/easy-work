from enterprises.models import Enterprise
from rest_framework import viewsets
from .models import Candidate, Education, Certificate, Site, Experience
from .serializers.candidate_serializer import CandidateListSerializer, CandidateDetailSerializer
from .serializers.education_serializer import EducationListSerializer, EducationDetailSerializer
from .serializers.certificate_serializer import CertificatDetailSerializer, CertificateListSerializer
from .serializers.site_serializers import SiteDetailCandidateSerializer, SiteListSerializer
from .serializers.experience_serializer import ExperiencesDetailSerializer, ExperiencesListSerializer



class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateDetailSerializer
    queryset = Candidate.objects.all()
    
    def get_serializer_class(self):
        if self.action=='list':
            return CandidateListSerializer
        return super().get_serializer_class()

class EducationViewSet(viewsets.ModelViewSet):
    serializer_class = EducationDetailSerializer
    def get_queryset(self):
        return Education.objects.filter(candidate=self.kwargs['candidate_id'])

    def get_serializer_class(self):
        if self.action=='list':
            return EducationListSerializer
        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        request.data['candidate'] = kwargs['candidate_id']
        return super().create(request, *args, **kwargs)

class CertificateViewSet(viewsets.ModelViewSet):
    serializer_class = CertificatDetailSerializer
    
    def get_queryset(self):
        return Certificate.objects.filter(candidate=self.kwargs['candidate_id'])
    
    def get_serializer_class(self):
        if self.action=='list':
            return CertificateListSerializer
        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        request.data['candidate'] = kwargs['candidate_id']
        return super().create(request, *args, **kwargs)

class SiteViewSet(viewsets.ModelViewSet):
    serializer_class = SiteDetailCandidateSerializer
    
    def get_queryset(self):
        return Site.objects.filter(owner=Candidate.objects.get(pk=self.kwargs['candidate_id']).user)
    
    def get_serializer_class(self):
        if self.action=='list':
            return SiteListSerializer
        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        request.data['owner'] = Candidate.objects.get(pk=kwargs['candidate_id']).user.id
        return super().create(request, *args, **kwargs)

class ExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = ExperiencesDetailSerializer
    
    def get_queryset(self):
        return Experience.objects.filter(candidate=self.kwargs['candidate_id'])
    
    def get_serializer_class(self):
        if self.action=='list':
            return ExperiencesListSerializer
        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        request.data['candidate'] = kwargs['candidate_id']
        return super().create(request, *args, **kwargs)