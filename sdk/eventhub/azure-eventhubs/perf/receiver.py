import time
from azure.eventhub import EventData
from perf.utils import WorkThread
from perf.config import MESSAGE_SAMPLES
from perf.client import get_client


class ReceiverThread(WorkThread):
    def work(self):
        received = self.worker.receive(timeout=5)
        self.cnt += len(received)


if __name__ == '__main__':
    client, eh_properties, partition_ids = get_client()
    threads = []
    for pid in partition_ids:
        receiver = client.create_receiver(partition_id=pid)
        receiver_thread = ReceiverThread(receiver, eh_properties["path"], pid)
        receiver_thread.start()

    for thread in threads:
        thread.join()
