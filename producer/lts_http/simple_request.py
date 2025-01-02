
class LtsRequest(object):

    def __init__(self, method, host, headers, body, region, interface, ak, sk):
        self.body = body
        self.method = method
        self.headers = headers
        self.host = host
        self.query = {}
        self.region = region
        self.interface = interface
        self.ak = ak
        self.sk = sk
