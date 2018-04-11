#!/usr/bin/python
# encoding: utf-8

"""
@auth: zhaopan
@time: 2018/3/30 15:26
"""
from proxy2 import *

class ProxyZCBLHandler(ProxyRequestHandler):

    def request_handler(self, req, req_body):
        pass

    def response_handler(self, req, req_body, res, res_body):
        host = req.headers.get('host')
        if host.endswith(".zhongchebaolian.com"):
            type = res.headers.type
            if type == "text/html":
                # insert js to head end
                src = "</head>"
                dest = "<script src=\"//qdota.com/bjjj/auto_commit.js\" charset=\"utf-8\"></script></head>"
                res_body.replace(src, dest)
                return res_body


if __name__ == '__main__':
    test(HandlerClass=ProxyZCBLHandler)
