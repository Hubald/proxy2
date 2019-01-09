from proxy2 import *
class Remove_Header_Acunetix(ProxyRequestHandler):
	def request_handler(self, req, req_body):
		#req.headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 5.01; Windows 98)'
		a = ['Acunetix-Product', 'Acunetix-Scanning-agreement', 'Acunetix-User-agreement']
		for i in a:
			for g in req.headers.keys():
				if i.lower() in g:
					del req.headers[g]
		print(req.headers)
start_server(HandlerClass=Remove_Header_Acunetix)