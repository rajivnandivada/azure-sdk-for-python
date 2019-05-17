# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LoadBalancerSku(Model):
    """SKU of a load balancer.

    :param name: Name of a load balancer SKU. Possible values include:
     'Basic', 'Standard'
    :type name: str or
     ~azure.mgmt.network.v2019_02_01.models.LoadBalancerSkuName
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(LoadBalancerSku, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)