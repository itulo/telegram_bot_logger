import datetime
import json

class EDiscussion:
    def create_from_discussion(self, discussion):
    	self.channel = discussion.chat.title
        self.text = discussion.text
        self.user = discussion.from_user.first_name
        self.date = datetime.datetime.fromtimestamp(discussion.date).strftime('%Y-%m-%d')
        return self

    def create_from_attributes(self, attrs):
    	self.channel = attrs[0]
    	self.text = attrs[1]
    	self.user = attrs[2]
    	self.date = attrs[3]
    	return self