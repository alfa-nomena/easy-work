from rest_framework import serializers
from candidates.models import Education


class EducationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = 'id', 'institut', 'diplom', 'period'