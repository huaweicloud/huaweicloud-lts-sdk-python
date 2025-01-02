import unittest

from producer.core.accumulator import Accumulator
from producer import Config
from producer import generate_log


class MyTestCase(unittest.TestCase):

    def test_add_multi_log_to_log_batch_map(self):
        config = Config()

        accumulator = Accumulator(config)
        logs_str = ["this is my first log"]
        labels = {"key1": "value1", "key2": "value2"}
        logs = generate_log(logs_str, labels)
        group_id = "group_1"
        stream_id = "stream_1"
        accumulator.add_log_to_log_batch_map(logs, group_id, stream_id, None)
        group_id_2 = "group_2"
        stream_id_2 = "stream_2"
        second_key = accumulator.get_log_batch_key(group_id_2, stream_id_2)
        accumulator.add_log_to_log_batch_map(logs, group_id_2, stream_id_2, None)
        self.assertEqual(len(accumulator.log_batch_map), 2)
        second_batch = accumulator.log_batch_map[second_key]
        self.assertEqual(len(second_batch.log_group.log_items), 1)

        accumulator.add_log_to_log_batch_map(logs, group_id_2, stream_id_2, None)
        self.assertEqual(len(accumulator.log_batch_map), 2)
        self.assertEqual(len(second_batch.log_group.log_items), 2)

    def test_add_one_log_to_log_batch_map(self):
        config = Config()
        accumulator = Accumulator(config)
        logs_str = ["this is my first log"]
        labels = {"key1": "value1", "key2": "value2"}
        logs = generate_log(logs_str, labels)
        group_id = "group_1"
        stream_id = "stream_1"
        first_key = accumulator.get_log_batch_key(group_id, stream_id)
        accumulator.add_log_to_log_batch_map(logs, group_id, stream_id, None)
        self.assertEqual(len(accumulator.log_batch_map), 1)
        first_batch = accumulator.log_batch_map[first_key]
        self.assertEqual(len(first_batch.log_group.log_items), 1)

        accumulator.add_log_to_log_batch_map(logs, group_id, stream_id, None)
        self.assertEqual(len(accumulator.log_batch_map), 1)
        self.assertEqual(len(first_batch.log_group.log_items), 2)

    def test_add_one_log_immediately_send(self):
        config = Config()
        config.batch_size_threshold_in_bytes = 2
        config.batch_count_threshold = 2
        accumulator = Accumulator(config)
        logs_str = ["this is my first log"]
        labels = {"key1": "value1", "key2": "value2"}
        logs = generate_log(logs_str, labels)
        group_id = "group_1"
        stream_id = "stream_1"
        first_key = accumulator.get_log_batch_key(group_id, stream_id)
        accumulator.add_log_to_log_batch_map(logs, group_id, stream_id, None)
        self.assertEqual(len(accumulator.log_batch_map), 1)
        first_batch = accumulator.log_batch_map[first_key]
        self.assertEqual(len(first_batch.log_group.log_items), 1)

        accumulator.add_log_to_log_batch_map(logs, group_id, stream_id, None)
        self.assertEqual(len(accumulator.log_batch_map), 0)


if __name__ == '__main__':
    unittest.main()
