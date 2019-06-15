import os
from azure.eventhub import EventHubClient


def get_client():
    con_str = os.environ["EVENT_HUBS_PERF_CON_STR"]
    client = EventHubClient.from_connection_string(con_str, event_hub_path="perf_event_hubs")
    eh_properties = client.get_properties()
    partition_ids = eh_properties["partition_ids"]

    return client, eh_properties, partition_ids
