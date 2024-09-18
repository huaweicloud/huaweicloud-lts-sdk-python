import time
import unittest

from loguru import logger

from producer.model.log import LogContent, LogGroup
from producer import generate_log
from producer.utils.common import convert_obj2_json_str


class LogTestCase(unittest.TestCase):
    def test_construct_log_content(self):
        log_content = LogContent(time.time_ns(), "this is my first log")
        logger.info("log content length is {}", len(log_content))
        self.assertGreater(len(log_content), 20)  # add assertion here

        log_content_str = convert_obj2_json_str(log_content)
        logger.info("log content convert json type is {}", type(log_content_str))
        logger.info("log content convert json is {}", log_content_str)

    def test_construct_log_group(self):
        logs_str = ["this is my first log"]
        labels = {"key1": "value1", "key2": "value2"}
        log_data = generate_log(logs_str, labels)
        logs = [log_data]
        log_group = LogGroup(log_items=logs)
        logger.info("log group size is {}", len(log_group))

    def test_time(self):
        logger.info(time.time())
        logger.info(int((time.time() * 1000)))
        logger.info(time.time_ns())


if __name__ == '__main__':
    unittest.main()
