from django.conf import settings
from netbox.plugins import PluginMenuItem, PluginMenuButton

# compatibility with netbox v3.3 that does not have PluginMenu
try:
    from netbox.plugins import PluginMenu
    HAVE_MENU = True
except ImportError:
    HAVE_MENU = False
    PluginMenu = PluginMenuItem


app_buttons = [
    PluginMenuItem(
        link='plugins:business_application:businessapplication_list',
        link_text='Business Applications',
        permissions=['business_application.view_businessapplication'],
        buttons=[
            PluginMenuItem(
                link='plugins:business_application:businessapplication_add',
                link_text='Add Business Application',
                permissions=['business_application.add_businessapplication'],
            ),
        ]
    )
]
if (HAVE_MENU and settings.PLUGINS_CONFIG['netbox_inventory']['top_level_menu']):
    # add a top level entry
    menu = PluginMenu(
        label=f'Bussiness Applications',
        groups=(
            ('Applications', app_buttons),
        ),
        icon_class='mdi mdi-clipboard-text-multiple-outline'
    )
else:
    # display under plugins
    menu_items = app_buttons