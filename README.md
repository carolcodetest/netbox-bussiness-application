# NetBox Plugin: Business Application

This plugin adds functionality to NetBox for managing business applications and their relationships to virtual machines.

## Features
- Manage business applications with fields:
  - `name`, `appcode`, `description`, `owner`, `delegate`, `servicenow` (link)
- Associate business applications with virtual machines.
- List and detail views for business applications in NetBox.
- Full CRUD operations via the NetBox UI and REST API.

## Installation

1. Clone the repository or download the plugin.
2. Install the plugin into your NetBox environment:
   ```bash
   pip install /path/to/plugin
   ```
3. Enable the plugin in your `configuration.py` file:
   ```python
   PLUGINS = ['business_application']
   PLUGINS_CONFIG = {
       'business_application': {}
   }
   ```
4. Run migrations:
   ```bash
   python /opt/netbox/netbox/manage.py migrate
   ```
5. Restart NetBox:
   ```bash
   sudo systemctl restart netbox netbox-rq
   ```

## Usage

- Navigate to the **Plugins** section in NetBox to manage business applications.
- Use the REST API to interact programmatically with business applications.

## Development

For contributing or development purposes, clone this repository and use the following setup:

```bash
pip install -r requirements.txt
```

## License

This plugin is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
