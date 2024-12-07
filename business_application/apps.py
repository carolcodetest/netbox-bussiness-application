from netbox.plugins import PluginConfig

class BusinessApplicationConfig(PluginConfig):
    name = "business_application"  # Must match the plugin directory name
    verbose_name = "Business Application"
    description = "Manage business applications and their relationships to virtual machines"
    version = "1.0.0"
    author = "Your Name"
    author_email = "your.email@example.com"
    base_url = "business-application"  # URL base for the plugin
    required_settings = []  # Define required settings if applicable
    min_version = "4.1.0"  # Minimum required NetBox version
    max_version = "4.1.99"  # Minimum required NetBox version
    default_settings = {
        'device_ext_page': 'right',
        'top_level_menu' : True,
    }
# Required for NetBox to recognize the plugin
config = BusinessApplicationConfig
