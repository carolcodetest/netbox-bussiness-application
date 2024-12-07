import django_tables2 as tables
from netbox.tables import NetBoxTable
from .models import BusinessApplication

class BusinessApplicationTable(NetBoxTable):
    name = tables.Column(linkify=True)
    appcode = tables.Column()
    owner = tables.Column()
    delegate = tables.Column()
    servicenow = tables.URLColumn(verbose_name="ServiceNow")

    class Meta(NetBoxTable.Meta):
        model = BusinessApplication
        fields = ['name', 'appcode', 'owner', 'delegate', 'servicenow']
