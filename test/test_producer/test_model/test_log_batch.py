import unittest

from loguru import logger

from producer import log_batch
from producer.model import lts_store
from producer import Config
from producer.utils.common import convert_obj2_json_str


class MyTestCase(unittest.TestCase):
    def test_init_log_batch(self):
        logs_str = ["this is my first log"]
        labels = {"key1": "value1", "key2": "value2"}
        logs = lts_store.generate_log(logs_str, labels)
        config = Config()
        _log_batch = log_batch.init_product_batch_var_single_log(logs, None, "group_id", "stream_id", config)
        log_content_str = convert_obj2_json_str(_log_batch)
        logger.info("log batch convert json is {}", log_content_str)


if __name__ == '__main__':
    unittest.main()
