import math
import time
import unittest

from loguru import logger

from producer.utils import common


class MyTestCase(unittest.TestCase):
    def test_current_time_ms(self):
        logger.info("now ns {}", time.time_ns())
        logger.info("now ms {}", common.current_time_ms())
        logger.info(math.pow(2, 3))

    def test_dict_operator(self):
        dict_op = {"name": "zhangsan", "age": "18", "sex": "male"}
        if "name" in dict_op:
            logger.info("key in dict")



if __name__ == '__main__':
    unittest.main()
