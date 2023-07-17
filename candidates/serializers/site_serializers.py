from mixins.user_serializer import UserSerializer
from rest_framework import serializers
from candidates.models import Site

class SiteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = 'id', 'title', 'link'

class SiteDetailCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = 'id', 'title', 'link', 'description', 'owner'
        extra_kwargs = {
            'owner': {'write_only': True},
        }