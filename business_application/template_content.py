from netbox.plugins import PluginTemplateExtension

from .models import BusinessApplication
from .tables import BusinessApplicationTable

class AppCodeExtension(PluginTemplateExtension):
    def left_page(self):
        if self.context['config'].get('device_ext_page') == 'left':
            return self.x_page()
        return ''

    def right_page(self):
        if self.context['config'].get('device_ext_page', 'right') == 'right':
            return self.x_page()
        return ''

    def full_width_page(self):
        if self.context['config'].get('device_ext_page') == 'full_width':
            return self.x_page()
        return ''

    def _get_query(self, obj):
        pass

    def x_page(self):
        obj = self.context['object']
        return self.render(
            'business_application/extend.html',
            extra_context={
                'related_appcodes': self._get_query(obj)
            }
        )


class DeviceAppCodeExtension(AppCodeExtension):
    model = 'dcim.device'
    def _get_query(self, obj):
        return BusinessApplicationTable(
            BusinessApplication.objects.filter(devices=obj)
        )

class VMAppCodeExtension(AppCodeExtension):
    model = 'virtualization.virtualmachine'
    def _get_query(self, obj):
        return BusinessApplicationTable(
            BusinessApplication.objects.filter(virtual_machines=obj)
        )

template_extensions = [
    DeviceAppCodeExtension,
    VMAppCodeExtension
]