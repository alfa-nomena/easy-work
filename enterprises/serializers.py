from rest_framework import serializers
from django.contrib.auth.models import User
from candidates.serializers.experience_serializer import ExperiencesListSerializer
from .models import Enterprise
from mixins.user_serializer import UserSerializer
from candidates.serializers.site_serializers import SiteListSerializer
# from jobs.serializers import JobListSerializer

class EnterpriseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = 'id', 'picture', 'title', 'size', 'name', 'email'
    
class EnterpriseDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(write_only=True)
    site_set = SiteListSerializer(many=True, read_only=True)
    # jobs = JobListSerializer(many=True)
    class Meta:
        model = Enterprise
        fields = 'id', 'picture', 'title', 'size', 'description', 'address', 'date_founded', 'user','site_set'
        extra_kwargs = {
            'user':{'write_only':True}
        }
        
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        return Enterprise.objects.create(user=user, **validated_data)