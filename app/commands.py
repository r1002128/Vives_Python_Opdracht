from .database import Database
from .models import Observation, Abbrev

class Commands:
	def __init__(self, dbPath):
		self.db = Database(dbPath)
	
	def get_abbrev_by_id(self, abbrev_id):
		query = f"SELECT * FROM Abbrev WHERE abbrev_id={abbrev_id}"
		result = self.db.return_query_results(query)
		print(result)

	def add_abbrev(self, abbrev_id, abbrev_text):
		query = f"""
		INSERT INTO Abbrev (abbrev_id, abbrev)
		VALUES ('{abbrev_id}', '{abbrev_text}');
		"""
		self.db.run_query(query)

	def close(self):
		self.db.close()