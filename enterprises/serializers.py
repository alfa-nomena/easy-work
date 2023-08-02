from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Enterprise
from mixins.user_serializer import UserSerializer
from candidates.serializers.site_serializers import SiteListSerializer
# from jobs.serializers import JobListSerializer

class EnterpriseListSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Enterprise
        fields = 'id', 'picture', 'title', 'size', 'name', 'email', 'description', 'date_founded','address'


    
class EnterpriseDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(write_only=True)
    site_set = SiteListSerializer(many=True, read_only=True)
    # jobs = JobListSerializer(many=True)
    class Meta:
        model = Enterprise
        fields = 'id', 'picture', 'title', 'size', 'description', 'address', 'date_founded', 'user','site_set'
        
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        return Enterprise.objects.create(user=user, **validated_data)