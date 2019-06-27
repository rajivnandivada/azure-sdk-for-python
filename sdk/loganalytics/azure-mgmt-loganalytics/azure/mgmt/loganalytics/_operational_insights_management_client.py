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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import OperationalInsightsManagementClientConfiguration
from .operations import LinkedServicesOperations
from .operations import DataSourcesOperations
from .operations import WorkspacesOperations
from .operations import Operations
from . import models


class OperationalInsightsManagementClient(SDKClient):
    """Operational Insights Client

    :ivar config: Configuration for client.
    :vartype config: OperationalInsightsManagementClientConfiguration

    :ivar linked_services: LinkedServices operations
    :vartype linked_services: azure.mgmt.loganalytics.operations.LinkedServicesOperations
    :ivar data_sources: DataSources operations
    :vartype data_sources: azure.mgmt.loganalytics.operations.DataSourcesOperations
    :ivar workspaces: Workspaces operations
    :vartype workspaces: azure.mgmt.loganalytics.operations.WorkspacesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.loganalytics.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = OperationalInsightsManagementClientConfiguration(credentials, subscription_id, base_url)
        super(OperationalInsightsManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2015-11-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.linked_services = LinkedServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.data_sources = DataSourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
