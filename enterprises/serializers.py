from rest_framework import serializers

from candidates.serializers.experience_serializer import ExperiencesListSerializer
from .models import Enterprise
from mixins.user_serializer import UserSerializer
from candidates.serializers.site_serializers import SiteListSerializer
from jobs.serializers import JobListSerializer

class EnterpriseListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Enterprise
        fields = 'id', 'logo', 'user', 'title', 'size'
    
class EnterpriseDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    sites = SiteListSerializer(many=True)
    experiences = ExperiencesListSerializer(many=True)
    jobs = JobListSerializer(many=True)
    class Meta:
        model = Enterprise
        fields = 'id', 'user', 'logo', 'title', 'size', 'description', 'address', 'founded_date', 'sites', 'experiences', 'jobs'