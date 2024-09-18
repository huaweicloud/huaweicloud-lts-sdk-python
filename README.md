## 1. 使用前提

- 要使用LTS Python SDK ，您需要拥有云账号以及该账号对应的 Access Key（AK）和 Secret Access Key（SK）。
  请在华为云控制台“我的凭证-访问密钥”页面上创建和查看您的 AK&SK
  。更多信息请查看 [访问密钥](https://support.huaweicloud.com/usermanual-ca/zh-cn_topic_0046606340.html)  。
- 要使用LTS Python SDK 上报日志
  ，您需要确认已在 [华为云控制台](https://console.huaweicloud.com/console/?locale=zh-cn&region=cn-north-4#/home) 开通LTS服务
- LTS Python SDK 适用于
    - python 3.10.1 及以上版本

## 2. Python-SDK使用的三方库

LTS Python SDK使用了以下第三方库

| 三方库      | 版本      |
|----------|---------|
| requests | 2.32.3  |
| loguru   | 0.7.2   |
| six      | 1.16.0  |



## 4. 代码配置

使用LTS python SDK时，有以下配置参数：

| 参数名称         | 描述                      | 类型     | 是否必填 | 默认值        |
|--------------|-------------------------|--------|------|------------|
| projectId    | 华为云帐号的项目ID（project id）。 | String | 必填   |            |
| ak           | 华为云帐号的AK。               | String | 必填   |            |
| sk           | 华为云帐号的SK。               | String | 必填   |            |
| region       | 云日志服务的区域。               | String | 必填   |            |
| endpoint     | 日志上报的目的地址。              | String | 必填   |            |
| logGroup     | 上报日志的日志组。               | String | 必填   |            |
| logStream    | 上报日志的日志流。               | String | 必填   |            |

## 5. 代码示例
```python
import random
import time
from concurrent.futures import ThreadPoolExecutor

from loguru import logger

from producer.core.producer import Producer
from producer.model import lts_store
from producer.model.config import Config
from producer.utils import common


def generate_random_str(str_len=16):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(str_len):
        random_str += base_str[random.randint(0, length)]
    return random_str

def send_log_single_producer():
    thread_num = 100
    threads = []
    submit_send_log_thread_pool = ThreadPoolExecutor(max_workers=thread_num, thread_name_prefix="send_log_thread")

    config = Config()
    config.endpoint = ""
    config.access_key = ""
    config.access_secret = ""
    config.region_id = ""
    config.project_id = ""
    producer = Producer.init_producer(config)
    producer.start_producer()

    group_id = ""
    stream_id = ""

    log_content = generate_random_str(1024)
    log = [log_content]
    labels = {"keyA": "valueA"}
    log_p = lts_store.generate_log(log, labels)

    for i in range(thread_num):
        new_thread = submit_send_log_thread_pool.submit(send_log_function, producer, group_id, stream_id, log_p)
        threads.append(new_thread)

    for t in threads:
        t.result()


def send_log_function(one_producer, group_id, stream_id, log_p):
    for i in range(2000):
        one_producer.send_log(group_id, stream_id, log_p)


if __name__ == '__main__':
    send_log_single_producer()
    time.sleep(1000)
```
