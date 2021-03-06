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


class RegenerateAccessKeyParameters(Model):
    """Parameters supplied to the Regenerate Authorization Rule operation,
    specifies which key needs to be reset.

    All required parameters must be populated in order to send to Azure.

    :param key_type: Required. The access key to regenerate. Possible values
     include: 'PrimaryKey', 'SecondaryKey'
    :type key_type: str or ~azure.mgmt.servicebus.models.KeyType
    :param key: Optional, if the key value provided, is reset for KeyType
     value or autogenerate Key value set for keyType
    :type key: str
    """

    _validation = {
        'key_type': {'required': True},
    }

    _attribute_map = {
        'key_type': {'key': 'keyType', 'type': 'KeyType'},
        'key': {'key': 'key', 'type': 'str'},
    }

    def __init__(self, *, key_type, key: str=None, **kwargs) -> None:
        super(RegenerateAccessKeyParameters, self).__init__(**kwargs)
        self.key_type = key_type
        self.key = key
