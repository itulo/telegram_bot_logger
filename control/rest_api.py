import web
from cdiscussion import CDiscussion

URLS = (
	'/discussion', 'list_discussions',
	'/discussion/(\d+)', 'get_discussion'
)

class list_discussions:
	def GET(self):
		web.header('Content-Type', 'application/json')
		return CDiscussion.list_discussion(web.input())

class get_discussion:
	def GET(self,id):
		print id
		web.header('Content-Type', 'application/json')
		return CDiscussion.get_discussion(id)


class Rest_api:
	def __init__(self):
		self.app = web.application(URLS, globals())

	def run(self):
		self.app.run()