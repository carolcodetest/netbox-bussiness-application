from django.conf import settings
from netbox.plugins import PluginMenuItem, PluginMenu, PluginMenuButton


_menu_items = (
    PluginMenuItem(
        link='plugins:business_application:businessapplication_list',
        link_text='Business Applications',
    ),
)


menu = PluginMenu(
    label="Business Application",
    groups=(("Application", _menu_items),),
    icon_class="mdi mdi-apps",
)
