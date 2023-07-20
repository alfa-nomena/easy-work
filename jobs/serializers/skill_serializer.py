from rest_framework import serializers
from jobs.models import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = 'title', 'id'