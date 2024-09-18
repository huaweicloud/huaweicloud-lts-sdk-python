PARAMETER_ERROR_CODE = "0000001"
ADD_LOG_TO_BATCH_ERROR_CODE = "0000002"
ADD_LOG_WAIT_TIMEOUT_ERROR_CODE = "0000003"
HTTP_QUEST_ERROR_CODE = "0000004"


class Error(object):
    def __init__(self, error_code: str, error_msg: str, http_code: int = 0, request_id: str = ""):
        self.http_code = http_code
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
