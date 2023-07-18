from rest_framework import viewsets
from .serializers.job_serializers import JobListSerializer, JobDetailSerializer
from .models import Job
from candidates.models import Candidate
from rest_framework.decorators import action

class JobViewset(viewsets.ModelViewSet):
    serializer_class = JobDetailSerializer
    queryset = Job.objects.all()
    
    def get_serializer_class(self):
        if self.action=='list':
            return JobListSerializer
        return super().get_serializer_class()
    
    def get_queryset(self):
        if self.kwargs['enterprise_id']:
            return Job.objects.filter(enterprise=self.kwargs['enterprise_id'])
        return super().get_queryset()