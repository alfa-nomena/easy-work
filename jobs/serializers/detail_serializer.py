from rest_framework import serializers
from jobs.models import Role, Profil


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = 'title', 'id'

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = 'title', 'id'