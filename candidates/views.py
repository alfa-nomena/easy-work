from rest_framework import viewsets
from .models import Candidate, Education, Certificate
from .serializers.candidate_serializer import CandidateListSerializer, CandidateDetailSerializer
from .serializers.education_serializer import EducationListSerializer, EducationDetailSerializer
from .serializers.certificate_serializer import CertificatDetailSerializer, CertificateListSerializer




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