from azure.eventhub import EventData
from perf.utils import WorkThread
from perf.config import MESSAGE_SAMPLES
from perf.client import get_client


class SenderThread(WorkThread):
    def work(self):
        msg = MESSAGE_SAMPLES[self.cnt % len(MESSAGE_SAMPLES)]
        self.worker.send(EventData(body=msg))
        self.cnt += 1


if __name__ == '__main__':
    client, eh_properties, partition_ids = get_client()
    threads = []
    for pid in partition_ids:
        sender = client.create_sender(partition_id=pid)
        sender_thread = SenderThread(sender, eh_properties["path"], pid)
        sender_thread.start()

    for thread in threads:
        thread.join()
