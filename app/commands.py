import csv

from .database import Database
from .models import Observation, Abbrev

class Commands:
	def __init__(self, dbPath):
		self.db = Database(dbPath)

	def close(self):
		self.db.close()
	
	def get_abbrev_by_id(self, abbrev_id):
		query = f"SELECT * FROM Abbrev WHERE abbrev_id={abbrev_id}"
		result = self.db.return_query_results(query)
		print(f'Resultaat voor de gegeven ID is: {result}')

	def add_abbrev(self, abbrev_id, abbrev_text):
		query = f"""
		INSERT INTO Abbrev (abbrev_id, abbrev)
		VALUES ('{abbrev_id}', '{abbrev_text}');
		"""
		self.db.run_query(query)

	def export_table_to_csv_file(self, csv_file, table_name):
		query = f"SELECT * FROM {table_name};"
		queryResult = self.db.return_query_results(query)

		with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file_writer:
			csv_writer = csv.writer(csv_file_writer)
			csv_writer.writerow(['ID', 'Abbrev'])
			csv_writer.writerows(queryResult)
		print(f'{table_name} is weggeschreven in {csv_file}')
