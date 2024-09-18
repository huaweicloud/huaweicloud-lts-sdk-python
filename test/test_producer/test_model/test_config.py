import unittest

from loguru import logger

from producer import Config
from producer.utils.common import convert_obj2_json_str


class MyTestCase(unittest.TestCase):
    def test_config_construct(self):
        config = Config()
        logger.info("config convert json is {}", convert_obj2_json_str(config))

        other_config = config.validate_config()
        logger.info("config convert json is {}", convert_obj2_json_str(other_config))


if __name__ == '__main__':
    unittest.main()
