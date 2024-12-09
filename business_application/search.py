from netbox.search import SearchIndex
from .models import BusinessApplication

class BusinessApplicationIndex(SearchIndex):
    model = BusinessApplication
    fields = (
        ('name', 100),
        ('appcode', 60),
        ('owner', 1000),
        ('delegate', 2000)
    )

indexes = [
    BusinessApplicationIndex
]