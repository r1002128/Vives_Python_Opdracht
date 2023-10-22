import sqlite3

class Database:
	def __init__(self, db_path):
		self.db_path = db_path
		self.connection = None

	def connect(self):
		if self.connection is None:
			self.connection = sqlite3.connect(self.db_path)
		return self.connection

	def close(self):
		if self.connection is not None:
			self.connection.close()
			self.connection = None

	def run_query(self,query):
		connection = self.connect()
		cursor = connection.cursor()	
		cursor.execute(query)
		connection.commit()
		return cursor

	def return_query_results(self,query):
		cursor = self.run_query(query)
		result = cursor.fetchall()
		cursor.close()
		return result
