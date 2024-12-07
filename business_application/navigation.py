from django.conf import settings
from netbox.plugins import PluginMenuItem, PluginMenuButton
from netbox.plugins import PluginNavigationMenu, PluginNavigationItem


# compatibility with netbox v3.3 that does not have PluginMenu
try:
    from netbox.plugins import PluginMenu
    HAVE_MENU = True
except ImportError:
    HAVE_MENU = False
    PluginMenu = PluginMenuItem

print('HERE')

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
plugin_settings = settings.PLUGINS_CONFIG.get('business_application', {})

if plugin_settings.get('top_level_menu', True):
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

navigation_menu = PluginNavigationMenu(
    items=[
        PluginNavigationItem(
            name="Business Applications",  # Display name in the menu
            link="plugins:business_application:businessapplication_list",  # Corresponds to the plugin's list view
            permissions=["business_application.view_businessapplication"],  # Required permissions
            icon_class="mdi mdi-apps",  # Optional: Material Design icon
        ),
    ]
)