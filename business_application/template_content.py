from netbox.plugins import PluginTemplateExtension
from django.db.models import Q

from .models import BusinessApplication
from .tables import BusinessApplicationTable
from virtualization.models import VirtualMachine
from dcim.models import Device

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

    def _get_related(self, obj):
        return BusinessApplicationTable(BusinessApplication.objects.none())

    def _get_downstream(self, obj):
        return BusinessApplicationTable(BusinessApplication.objects.none())

    def x_page(self):
        obj = self.context['object']
        return self.render(
            'business_application/extend.html',
            extra_context={
                'related_appcodes': self._get_related(obj),
                'downstream_appcodes': self._get_downstream(obj),
            }
        )


class DeviceAppCodeExtension(AppCodeExtension):
    model = 'dcim.device'
    def _get_related(self, obj):
        return BusinessApplicationTable(
            BusinessApplication.objects.filter(devices=obj)
        )

    def _get_downstream(self, obj):
        apps = set()
        nodes = [obj]
        current = 0
        while current < len(nodes):
            node = nodes[current]
            apps = apps.union(BusinessApplication.objects.filter(Q(devices=node) | Q(virtual_machines__device=node)))

            for cable_termination in node.cabletermination_set.all():
                for termination in cable_termination.cable.b_terminations:
                    if termination and termination.device and termination.device not in nodes:
                        nodes.append(termination.device)
                for termination in cable_termination.cable.a_terminations:
                    if termination and termination.device and termination.device.role == node.role and termination.device not in nodes:
                        nodes.append(termination.device)
            current += 1
        return BusinessApplicationTable(apps)

class VMAppCodeExtension(AppCodeExtension):
    model = 'virtualization.virtualmachine'
    def _get_related(self, obj):
        return BusinessApplicationTable(
            BusinessApplication.objects.filter(virtual_machines=obj)
        )

class ClusterAppCodeExtension(AppCodeExtension):
    model = 'virtualization.cluster'

    def right_page(self):
        obj = self.context['object']

        vms_in_cluster = VirtualMachine.objects.filter(cluster=obj)
        related_apps_via_vm = BusinessApplication.objects.filter(
            virtual_machines__in=vms_in_cluster
        ).distinct()

        downstream_apps_set = set()
        processed_devices_ids = set()

        for vm in vms_in_cluster:
            downstream_apps_set.update(BusinessApplication.objects.filter(virtual_machines=vm))        
            if vm.device and vm.device.id not in processed_devices_ids:
                nodes_to_traverse = [vm.device]
                temp_visited_ids_for_path = {vm.device.id}
                current_node_index = 0

                while current_node_index < len(nodes_to_traverse):
                    current_device_node = nodes_to_traverse[current_node_index]

                    downstream_apps_set.update(BusinessApplication.objects.filter(
                        Q(devices=current_device_node) | Q(virtual_machines__device=current_device_node)
                    ))

                    for termination in current_device_node.cabletermination_set.all():
                        cable = termination.cable
                        for connected_termination in cable.a_terminations.all() + cable.b_terminations.all():
                            if hasattr(connected_termination, 'device') and connected_termination.device:
                                if connected_termination.device.id not in temp_visited_ids_for_path:
                                    nodes_to_traverse.append(connected_termination.device)
                                    temp_visited_ids_for_path.add(connected_termination.device.id)
                    current_node_index += 1
                processed_devices_ids.add(vm.device.id)

        return self.render(
            'business_application/extend.html',
            extra_context={
                'related_appcodes': BusinessApplicationTable(related_apps_via_vm),
                'downstream_appcodes': BusinessApplicationTable(list(downstream_apps_set)),
            }
        )

template_extensions = [
    DeviceAppCodeExtension,
    VMAppCodeExtension,
    ClusterAppCodeExtension,
]
