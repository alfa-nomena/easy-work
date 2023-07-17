from rest_framework import serializers
from candidates.models import Experience
# from .candidate_serializer import CandidateListSerializer

class ExperiencesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = 'id','period',  'title'

# class ExperienceDetailSerializer(serializers.ModelSerializer):
#     candidates = CandidateListSerializer(many=True)
#     class Meta:
#         model = Experience
#         fields = 'id','period', 'candidates', 'title', 'description'