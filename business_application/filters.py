from django_filters import FilterSet, CharFilter
from .models import BusinessApplication

class BusinessApplicationFilter(FilterSet):
    """
    Filters for the BusinessApplication model.
    """
    name = CharFilter(lookup_expr='icontains')
    appcode = CharFilter(lookup_expr='iexact')

    class Meta:
        model = BusinessApplication
        fields = ['name', 'appcode', 'owner', 'delegate']
