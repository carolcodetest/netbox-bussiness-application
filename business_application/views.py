from netbox.views import generic
from .models import BusinessApplication
from .forms import BusinessApplicationForm
from .tables import BusinessApplicationTable
from .filtersets import BusinessApplicationFilter

class BusinessApplicationListView(generic.ObjectListView):
    queryset = BusinessApplication.objects.all()
    table = BusinessApplicationTable
    filterset = BusinessApplicationFilter

class BusinessApplicationChangeLogView(generic.ObjectChangeLogView):
    queryset = BusinessApplication.objects.all()

class BusinessApplicationDetailView(generic.ObjectView):
    queryset = BusinessApplication.objects.all()
    template_name = 'business_application/businessapplication.html'

class BusinessApplicationCreateView(generic.ObjectEditView):
    queryset = BusinessApplication.objects.all()
    form = BusinessApplicationForm

class BusinessApplicationEditView(generic.ObjectEditView):
    queryset = BusinessApplication.objects.all()
    form = BusinessApplicationForm

class BusinessApplicationDeleteView(generic.ObjectDeleteView):
    queryset = BusinessApplication.objects.all()
