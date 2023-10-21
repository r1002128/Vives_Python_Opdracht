import sqlite3

class Database:
	def __init__(self,dbPath):
		try:
			self.dbConnectie = sqlite3.connect(dbPath)
		except:
			print("De database kon niet gevonden worden.")

		self.cursor = self.dbConnectie.cursor()

	def run_query(self,query):
		try:
			self.cursor.execute(query)
			self.dbConnectie.commit()
			print('Query uitgevoerd.')
		except e:
			print(e)

	def return_query_results(self,query):
		self.cursor.execute(query)
		return self.cursor.fetchall()

	def close():
		self.dbConnectie.close()

