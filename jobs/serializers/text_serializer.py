from rest_framework import serializers
from jobs.models import Detail


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = 'id', 'title'