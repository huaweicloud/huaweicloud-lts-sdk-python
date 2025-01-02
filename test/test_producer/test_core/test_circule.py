from producer.core.producer import Producer
from producer import Config

if __name__ == '__main__':
    config = Config()
    producer = Producer.init_producer(config)

