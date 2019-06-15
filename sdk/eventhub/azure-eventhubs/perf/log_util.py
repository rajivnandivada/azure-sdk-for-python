from logging import getLoggerClass, addLevelName, setLoggerClass, NOTSET
import logging


PERF = 100


def perf(self, message, *args, **kws):
    self.log(PERF, message, *args, **kws)


logging.Logger.perf = perf
logging.basicConfig(level=PERF)
logging.addLevelName(PERF, "PERF")
