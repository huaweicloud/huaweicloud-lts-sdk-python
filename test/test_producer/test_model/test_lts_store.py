import unittest

from loguru import logger

from producer import generate_log
from producer.utils.common import convert_obj2_json_str


class LtsStoreTestCase(unittest.TestCase):

    def test_generateLog(self):
        logs_str = ["this is my first log"]
        labels = {"key1": "value1", "key2": "value2"}
        logs = generate_log(logs_str, labels)
        log_str = convert_obj2_json_str(logs)
        logger.info("log convert json is {}", log_str)


if __name__ == '__main__':
    unittest.main()
