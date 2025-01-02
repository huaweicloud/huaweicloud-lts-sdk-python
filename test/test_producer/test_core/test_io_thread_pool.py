import threading
import unittest

from loguru import logger

from producer.core import io_thread_pool
from producer import log_batch
from producer.model import lts_store
from producer import Config


class MyTestCase(unittest.TestCase):
    def test_something(self):
        thread_pool = io_thread_pool.IOThreadPool()

        logs_str = ["this is my first log"]
        labels = {"key1": "value1", "key2": "value2"}
        logs = lts_store.generate_log(logs_str, labels)
        config = Config()
        _log_batch = log_batch.init_product_batch_var_single_log(logs, None, "group_id", "stream_id", config)

        class Thread1(threading.Thread):
            def run(self):
                thread_pool.add_task(_log_batch)
                logger.info("after thread1, thread pool size is {}", thread_pool.task_queue_size())

        class Thread2(threading.Thread):
            def run(self):
                thread_pool.add_task(_log_batch)
                logger.info("after thread2, thread pool size is {}", thread_pool.task_queue_size())

        Thread1().start()
        Thread2().start()
        self.assertEqual(thread_pool.task_queue_size(), 2)


if __name__ == '__main__':
    unittest.main()
