
class LtsRequest(object):

    def __init__(self, method, host, headers, body, region, interface, ak, sk, **kwargs):
        self.body = body
        self.method = method
        self.headers = headers
        self.host = host
        self.query = kwargs
        self.region = region
        self.interface = interface
        self.ak = ak
        self.sk = sk
