import unittest

from consumer.client.http_client import HttpClient
from loguru import logger


class MyTestCase(unittest.TestCase):
    def test_connect_query_string(self):
        query_map = {"key1": "value1", "key2": "value2", "key3": "value3"}
        url = "http://www.baidu.com"
        result = HttpClient.connect_query_string(query_map, url)
        logger.info("result url is {}", result)


