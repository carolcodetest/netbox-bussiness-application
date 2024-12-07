from django.conf import settings
from extras.plugins import PluginMenuItem



menu_items = (
    PluginMenuItem(
        link='plugins:business_application:businessapplication_list',
        link_text='Business Applications',
        permissions=['business_application.view_businessapplication'],
    ),
)
