import requests
import urllib3
from loguru import logger
from requests.adapters import HTTPAdapter
from urllib3.exceptions import InsecureRequestWarning
from urllib3.util.retry import Retry

from producer.auth.signer import Signer
from producer.lts_http.simple_request import LtsRequest
from producer.model import error
from producer.model.config import Config
from producer.model.log import LogGroup
from producer.utils import common


class HttpClient(object):
    def __init__(self):
        self._session = requests.Session()
        self._signer = Signer()

        retry_strategy = Retry(
            total=2,
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=1
        )
        adapter = HTTPAdapter(max_retries=retry_strategy, pool_connections=100, pool_maxsize=100)
        self._session.mount("https://", adapter)
        self._session.mount("http://", adapter)
        urllib3.disable_warnings(InsecureRequestWarning)

    def put_logs(self, group_id, stream_id, log_group: LogGroup, config: Config):
        if log_group is None or len(log_group.log_items) == 0:
            return None

        body = common.convert_obj2_json_str(log_group)
        header = {"content-type": "application/json"}

        interface = "/v2/internal/{0}/lts/groups/{1}/streams/{2}/tenant/batch-contents".format(config.project_id,
                                                                                               group_id, stream_id)

        req = LtsRequest(method="POST", host=config.endpoint, headers=header, body=body, region=config.region_id,
                         interface=interface, ak=config.access_key, sk=config.access_secret)
        request = self._signer.sign(req)
        r = request.prepare()
        try:
            response = self._session.send(r, verify=False)
            response.encoding = "utf-8"
            logger.info("send log status code {}, response is {}", response.status_code,
                        response.content.decode("utf-8"))
            if response.status_code == 200:
                return None
            else:
                return error.Error(error_code=error.HTTP_QUEST_ERROR_CODE, error_msg=response.content.decode("utf-8"),
                                   http_code=response.status_code)
        except Exception as e:
            logger.error("send log error {}", e)
            return error.Error(error_code=error.HTTP_QUEST_ERROR_CODE, error_msg=str(e), http_code=0)
