from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.common.credentials import ServicePrincipalCredentials

# subscription_id = 'XXXX'
# tenant_id = 'XXXX'
# client_id = 'XXXX'
# client_secret = 'XXXX'

subscription_id = '992c68c5-9c3d-4850-8787-90362899af5d'
tenant_id = '6a5f91fe-6a84-4d5b-a7f1-dbab8a01b1e4'
client_id = '6459304c-ce63-44a0-a60e-64aa81ec63dd'
client_secret = 'f2u7Q~yTJZk_9K4MJrLN7huxQ1OY-Beqx9Jk_'

credentials = ServicePrincipalCredentials(tenant=tenant_id, client_id=client_id, secret=client_secret)
resource_client = ResourceManagementClient(credentials, subscription_id)
compute_client = client = ComputeManagementClient(credentials, subscription_id)


def list_vms_in_subscription():
    group_list = resource_client.resource_groups.list()
    for group in list(group_list):
        list_vms_in_groups(group.name)

def list_vms_in_groups(group_name):
    for resource in resource_client.resources.list_by_resource_group(group_name):
        if resource.type == "Microsoft.Compute/virtualMachines":
            print(resource.name)

        if resource.type == "Microsoft.Compute/virtualMachineScaleSets":
            vmss = compute_client.virtual_machine_scale_set_vms.list(group_name, resource.name)
            for vm in vmss:
                print(vm.name)


if __name__ == '__main__':
    list_vms_in_subscription()
    # list = compute_client.virtual_machines.list('MC_alonresourcegroup_AKS_self_managed_eastus')
    # for vm in list:
    #     print (vm)

    subscription_id = '992c68c5-9c3d-4850-8787-90362899af5d'
    tenant_id = '6a5f91fe-6a84-4d5b-a7f1-dbab8a01b1e4'
    client_id = '6459304c-ce63-44a0-a60e-64aa81ec63dd'
    client_secret = 'f2u7Q~yTJZk_9K4MJrLN7huxQ1OY-Beqx9Jk_'