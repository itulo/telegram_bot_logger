import sqlite3

DB = 'discussions.db'
EQUALITY_OPT = ['user', 'date']
SIMILAR_OPT = ['text']

class DDiscussion:
	@staticmethod
	def open_connection():
		return sqlite3.connect(DB)

	@staticmethod
	def close_connection(conn):
		conn.close()

	@staticmethod
	def save(discussion):
		conn = DDiscussion.open_connection()
		conn.cursor().execute("INSERT INTO discussions VALUES (?,?,?,?)", 
			[discussion.channel, discussion.user, discussion.text, discussion.date])
		conn.commit()
		DDiscussion.close_connection(conn)

	@staticmethod
	def load(id):
		conn = DDiscussion.open_connection()
		row = conn.cursor().execute("SELECT * FROM discussions where rowid=?", [id])
		disc = row.fetchone()
		conn.close()
		return disc

	@staticmethod
	def load_many(options):
		discussions = []
		query = "SELECT * FROM discussions"
		cond = ""

		for i in EQUALITY_OPT:
			if i in options:
				cond += " LOWER(" + i + ")='" + options[i] + "' and"
		for i in SIMILAR_OPT:
			if i in options:
				cond += " " + i + " like '%" + options[i] + "%' and"

		if len(cond) > 0:
			query += " where " + cond[:-3]

		conn = DDiscussion.open_connection()
		for row in conn.cursor().execute(query):
			discussions.append(row)
		DDiscussion.close_connection(conn)

		return discussions

