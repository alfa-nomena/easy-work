from rest_framework import viewsets, response
from .serializers.job_serializers import JobListSerializer, JobDetailSerializer
from .models import Job, EXPERIENCES_PERIODS
from rest_framework.decorators import action

class JobViewset(viewsets.ModelViewSet):
    serializer_class = JobDetailSerializer
    queryset = Job.objects.all().order_by('-date_posted', 'title')
    
    def get_serializer_class(self):
        if self.action=='list':
            return JobListSerializer
        return super().get_serializer_class()
    
    def get_queryset(self):
        if self.kwargs.get('enterprise_id'):
            return Job.objects.filter(enterprise=self.kwargs['enterprise_id']).order_by('-date_posted', 'title')
        return super().get_queryset()
    
    @action(detail=False)
    def list_all_jobs(self, *args, **kwargs):
        list_queryset= self.paginate_queryset(Job.objects.all().order_by('-date_posted', 'title'))
        return self.get_paginated_response(JobListSerializer(list_queryset, many=True).data)
    
    @action(detail=False)
    def list_all_experience_periods(self, *args, **kwargs):
        return response.Response(EXPERIENCES_PERIODS)
    
    def create(self, request, *args, **kwargs):
        request.data['enterprise'] = kwargs['enterprise_id']
        return super().create(request, *args, **kwargs)