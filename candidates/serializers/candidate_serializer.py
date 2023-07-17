from rest_framework import serializers
from candidates.models import Candidate
from mixins.user_serializer import UserSerializer
from .experience_serializer import ExperiencesListSerializer
from .certificate_serializer import CertificateListSerializer
from .education_serializer import EducationListSerializer
from jobs.serializers.skill_serializer import SkillSerializer
from .site_serializers import SiteListSerializer
from django.contrib.auth.models import User

class CandidateListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Candidate
        fields = ('id', 'user', 'picture', 'address', 'title')
    
class CandidateDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    experiences = ExperiencesListSerializer(many=True, read_only=True)
    certificats = CertificateListSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    educations = EducationListSerializer(many=True, read_only=True)
    sites = SiteListSerializer(many=True, read_only=True)
    class Meta:
        model = Candidate
        fields = ('id', 'user', 'picture', 'cv', 'github', 'linkedin', 'phone1', 'phone2', 'address', 'title', 'about', 'skills', 'educations', 'sites', 'experiences', 'certificats')
        depth = 2
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        return Candidate.objects.create(user=user, **validated_data)