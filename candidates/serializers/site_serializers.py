from rest_framework import serializers
from candidates.models import Site

class SiteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = 'id', 'title', 'link'