from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import EnterpriseDetailSerializer, EnterpriseListSerializer, SectorSerializer
from .models import Enterprise, Sector
from candidates.serializers.site_serializers import SiteDetailSerializer, SiteListSerializer
from candidates.models import Site
class EnterpriseViewSet(viewsets.ModelViewSet):
    serializer_class = EnterpriseDetailSerializer
    queryset = Enterprise.objects.all()
    
    @action(detail=False)
    def list_sectors(self, *args, **kwargs):
        qs = SectorSerializer(data=Sector.objects.all(), many=True)
        qs.is_valid()
        return Response(qs.data)
    
    def get_serializer_class(self):
        if self.action=='list':
            return EnterpriseListSerializer
        return super().get_serializer_class()
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

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