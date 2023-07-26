from rest_framework import serializers
from enterprises.serializers import EnterpriseListSerializer
from jobs.models import Job
from .skill_serializer import SkillSerializer
from .detail_serializer import RoleSerializer, ProfilSerializer


class JobListSerializer(serializers.ModelSerializer):
    enterprise_display = EnterpriseListSerializer(read_only=True)
    class Meta:
        fields = 'id', 'title', 'enterprise_display', 'date_posted', 'type', 'address', 'contract', 'experience'
        model = Job
        ordering = ['date_posted', 'title']

class JobDetailSerializer(serializers.ModelSerializer):
    enterprise_display = EnterpriseListSerializer(read_only=True)
    skill_set = SkillSerializer(many=True, read_only=True)
    role_set = RoleSerializer(many=True, read_only=True)
    profil_set = ProfilSerializer(many=True, read_only=True)
    class Meta:
        fields = 'id', 'title', 'enterprise', 'date_posted', 'date_last_modified', 'type', 'address', 'contract', 'experience', 'experience_value', 'type_value', 'contract_value', 'enterprise_display', 'location', 'skill_set', 'profil_set', 'role_set'
        model = Job
        extra_kwargs = {
            'experience_value': {'write_only': True},
            'type_value': {'write_only': True},
            'contract_value': {'write_only': True},
            'enterprise': {'write_only': True}
        }
        