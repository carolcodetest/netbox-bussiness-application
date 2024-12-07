from extras.plugins import PluginNavigationMenu

navigation_menu = PluginNavigationMenu(
    items=[
        {
            'name': 'Business Applications',
            'url': 'plugins:business_application:businessapplication_list',
            'icon_class': 'mdi mdi-apps',
        },
    ]
)
