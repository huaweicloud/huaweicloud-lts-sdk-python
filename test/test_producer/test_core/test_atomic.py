import unittest

import atomics
from loguru import logger


class MyTestCase(unittest.TestCase):
    def test_something(self):
        task_count = atomics.atomic(width=4, atype=atomics.INT)
        task_count.store(2)
        task_count.inc()
        logger.info("task count is {}", task_count.load())


if __name__ == '__main__':
    unittest.main()
