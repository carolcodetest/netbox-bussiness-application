from netbox.filtersets import NetBoxModelFilterSet
from .models import BusinessApplication

class BusinessApplicationFilter(NetBoxModelFilterSet):
    """
    Filters for the BusinessApplication model.
    """
    
    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)

    class Meta:
        model = BusinessApplication
        fields = ['name', 'appcode', 'owner', 'delegate']
