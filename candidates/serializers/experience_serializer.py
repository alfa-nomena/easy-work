from rest_framework import serializers
from candidates.models import Experience
# from .candidate_serializer import CandidateListSerializer

class ExperiencesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = 'id','period', 'title'
class ExperiencesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = 'id','period', 'title', 'description', 'start', 'end', "candidate"
        extra_kwargs = {
            'start': {'write_only': True},
            'end': {'write_only': True},
            'candidate': {'write_only': True},
            'period': {'read_only':True}
        }