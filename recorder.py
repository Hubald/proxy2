from proxy2 import ProxyRequestHandler,test
import os
from pymongo import MongoClient
from datetime import datetime
from bson import Binary

port = int(os.getenv('MONGO_PORT', '27017'))
client = MongoClient('localhost', port)
db = client.rr
collection = db.requests

class RequestRecoder(ProxyRequestHandler):
    def save_handler(self, req, req_body, res, res_body):
        if len(res_body) < 10240:
            collection.insert_one({
                "timestamp": datetime.utcnow(),
                "req_command": req.command,
                "req_path": req.path,
                "req_version": req.request_version,
                "req_headers": dict(req.headers),
                "res_version": res.response_version,
                "res_status": res.status,
                "res_reason": res.reason,
                "res_headers": dict(res.headers),
                "req_body": Binary(bytes(req_body)) if req_body else req_body,
                "res_body": Binary(bytes(res_body)) if res_body else res_body
                })

if __name__ == '__main__':
    test(RequestRecoder)

