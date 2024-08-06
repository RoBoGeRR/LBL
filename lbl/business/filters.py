import django_filters

from .models import Business

class BusinessFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')
    address = django_filters.CharFilter(lookup_expr='icontains')
    latitude = django_filters.NumberFilter(lookup_expr='exact')
    latitude__gt = django_filters.NumberFilter(field_name='latitude', lookup_expr='gt')
    latitude__lt = django_filters.NumberFilter(field_name='latitude', lookup_expr='lt')
    longtitude = django_filters.NumberFilter(lookup_expr='exact')
    longtitude__gt = django_filters.NumberFilter(field_name='longtitude', lookup_expr='gt')
    longtitude__lt = django_filters.NumberFilter(field_name='longtitude', lookup_expr='lt')

    class Meta:
        model = Business
        
        fields = {
            'latitude',
            'longtitude',
            'name',
            'category',
            'address',
        }