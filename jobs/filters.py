import django_filters as filters
from .models import Job


class JobBasicFilter(filters.FilterSet):
    experience_value = filters.CharFilter()
    sector_set = filters.CharFilter(field_name='sector_set__title')
    class Meta:
        model=Job
        fields = ['experience_value', 'sector_set']