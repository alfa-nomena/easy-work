from rest_framework import viewsets
from .models import Candidate
from .serializers.candidate_serializer import CandidateListSerializer, CandidateDetailSerializer
from rest_framework.decorators import action

class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateDetailSerializer
    queryset = Candidate.objects.all()
    
    def get_serializer_class(self):
        if self.action=='list':
            return CandidateListSerializer
        return super().get_serializer_class()