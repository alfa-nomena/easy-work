from rest_framework import viewsets
from .serializers import EnterpriseDetailSerializer, EnterpriseListSerializer
from .models import Enterprise
from candidates.serializers.site_serializers import SiteDetailSerializer, SiteListSerializer
from candidates.models import Site

class EnterpriseViewSet(viewsets.ModelViewSet):
    serializer_class = EnterpriseDetailSerializer
    queryset = Enterprise.objects.all()
    
    def get_serializer_class(self):
        if self.action=='list':
            return EnterpriseListSerializer
        return super().get_serializer_class()
    

class SiteEnterpriseViewSet(viewsets.ModelViewSet):
    serializer_class = SiteDetailSerializer
    
    def get_queryset(self):
        return Site.objects.filter(owner=Enterprise.objects.get(pk=self.kwargs['enterprise_id']).user)
    
    def get_serializer_class(self):
        if self.action=='list':
            return SiteListSerializer
        return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        request.data['owner'] = Enterprise.objects.get(pk=kwargs['enterprise_id']).user.id
        return super().create(request, *args, **kwargs)