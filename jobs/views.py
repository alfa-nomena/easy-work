from rest_framework import viewsets, response
from .serializers.job_serializers import JobListSerializer, JobDetailSerializer
from .models import Job, EXPERIENCES_PERIODS
from rest_framework.decorators import action
from django.db.models import Q
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
    def list_filtered_jobs(self, *args, **kwargs):
        qs = Job.objects.all()
        params = self.request.query_params
        if params.get('experience'):
            qs = qs.filter(experience_value=params['experience'])
        if params.get('sector'):
            qs = qs.filter(enterprise__sector__title=params['sector'])
        if params.get('keyword'):
            qs = qs.filter(Q(enterprise__title__icontains=params['keyword'])|Q(title__icontains=params['keyword']))
            print(qs)
        list_queryset= self.paginate_queryset(qs.order_by('-date_posted', 'title'))
        return self.get_paginated_response(JobListSerializer(list_queryset, many=True).data)
    @action(detail=False)
    def list_all_experience_periods(self, *args, **kwargs):
        return response.Response(EXPERIENCES_PERIODS)
    
    @action(detail=True)
    def count_jobs(self, *args, **kwargs):
        return response.Response(Job.objects.all().count())
    
    def create(self, request, *args, **kwargs):
        request.data['enterprise'] = kwargs['enterprise_id']
        return super().create(request, *args, **kwargs)