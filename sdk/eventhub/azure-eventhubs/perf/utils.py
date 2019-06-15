import time
import logging
from abc import abstractmethod
from threading import Thread
from multiprocessing import Process

from perf.config import TEST_DURATION
from perf import log_util


class Worker(object):
    def __init__(self, worker, eh_name, partition_id):
        self.worker = worker
        self.eh_name = eh_name
        self.partition_id = partition_id
        self.logger = logging.getLogger(type(worker).__name__)
        self.logger.setLevel(log_util.PERF)
        self.cnt = 0  # count of event data processed
        super().__init__()

    def run(self):
        try:
            start_time = time.time()
            self.logger.perf("Started, %r, %r, %r", time.time(), self.eh_name, self.partition_id)
            while time.time() - start_time <= TEST_DURATION:
                self.work()
            self.logger.perf("Finished, %r, %r, %r, %r", time.time(), self.eh_name, self.partition_id, self.cnt)
        finally:
            self.worker.close()

    def work(self, cnt):
        pass


class WorkThread(Worker, Thread):
    def __init__(self, worker, eh_name, partition_id):
        super(WorkThread, self).__init__(worker, eh_name, partition_id)

    def run(self):
        super(WorkThread, self).run()


class WorkProcess(Worker, Process):
    def __init__(self, worker, eh_name, partition_id):
        super(WorkProcess, self).__init__(worker, eh_name, partition_id)

    def run(self):
        super(WorkProcess, self).run()