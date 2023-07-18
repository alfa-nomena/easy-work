from rest_framework import serializers
from jobs.models import Job



class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = 'id', 'title', 'enterprise', 'date_posted', 'type', 'address', 'contract', 'experience', 
        model = Job

class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = 'id', 'title', 'enterprise', 'date_posted', 'date_last_modified', 'type', 'address', 'contract', 'experience', 
        model = Job