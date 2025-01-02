import threading
import time

from loguru import logger

from producer.utils import lts_threading


class MyRead(threading.Thread):
    def __init__(self, rw_lock, num):
        super().__init__()
        self.rw_lock = rw_lock
        self.num = num

    def run(self):
        logger.info("my read {} start", self.num)
        self.rw_lock.acquire_read()
        try:
            logger.info("my read {} thread acquire read lock", self.num)
            time.sleep(5)
            logger.info("my read {} stop", self.num)
        finally:
            logger.info("my read {} release read lock", self.num)
            self.rw_lock.release_read()


class MyWrite(threading.Thread):
    def __init__(self, rw_lock, num):
        super().__init__()
        self.rw_lock = rw_lock
        self.num = num

    def run(self):
        logger.info("my write {} start", self.num)
        self.rw_lock.acquire_write()
        try:
            logger.info("my write {} thread acquire read lock", self.num)
            time.sleep(5)
            logger.info("my write {} stop", self.num)
        finally:
            logger.info("my write {} release read lock", self.num)
            self.rw_lock.release_write()


if __name__ == '__main__':

    rw_lock_outer = lts_threading.ReadWriteLock()
    for i in range(100):
        MyRead(rw_lock_outer, i).start()
    for i in range(100):
        MyWrite(rw_lock_outer, i).start()
