import json
from entity.ediscussion import EDiscussion
from database.ddiscussion import DDiscussion

ALLOWED_PARAMS = ['user', 'text', 'date']

class CDiscussion:
	@staticmethod
	def list_discussion(params):
		response = []
		opt = {}

		for i in ALLOWED_PARAMS:
			if i in params:
				opt[i] = params[i].lower()

		discussions = DDiscussion.load_many(opt)
		if len(discussions) > 0:
			for d in discussions:
				response.append(EDiscussion().create_from_attributes(d).__dict__)
		
		return json.dumps(response)

	@staticmethod
	def get_discussion(id):
		response = []

		attrs = DDiscussion.load(id)
		if attrs != None:
			disc = EDiscussion().create_from_attributes(attrs)
			response.append(disc.__dict__)

		return json.dumps(response)