from rest_framework import serializers
from candidates.models import Education


class EducationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = 'id', 'institut', 'diplom', 'period'

class EducationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = 'id', 'institut', 'diplom', 'period', 'description', "candidate", 'start', 'end'
        extra_kwargs = {
            'start': {'write_only': True},
            'end': {'write_only': True},
        }