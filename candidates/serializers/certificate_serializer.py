from rest_framework import serializers
from candidates.models import Certificate


class CertificateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = 'id', 'title', 'link', 'obtention_date', 'institut'

class CertificatDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = 'id', 'title', 'description', 'link', 'picture', 'obtention_date', 'institut', 'candidate'
