from netbox.views import generic
from .models import BusinessApplication
from .forms import BusinessApplicationForm
from .tables import BusinessApplicationTable
from .filters import BusinessApplicationFilter

class BusinessApplicationListView(generic.ObjectListView):
    queryset = BusinessApplication.objects.all()
    table = BusinessApplicationTable
    filterset = BusinessApplicationFilter
    template_name = "business_application/businessapplication/list.html"

class BusinessApplicationDetailView(generic.ObjectView):
    queryset = BusinessApplication.objects.all()
    template_name = "business_application/businessapplication/detail.html"

class BusinessApplicationCreateView(generic.ObjectEditView):
    queryset = BusinessApplication.objects.all()
    model_form = BusinessApplicationForm

class BusinessApplicationEditView(generic.ObjectEditView):
    queryset = BusinessApplication.objects.all()
    model_form = BusinessApplicationForm

class BusinessApplicationDeleteView(generic.ObjectDeleteView):
    queryset = BusinessApplication.objects.all()
