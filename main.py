from app.commands import Commands
from data.settings import DB_NAAM
import sys

commands = Commands(DB_NAAM)

command_name = input("Geef mee wat je wilt doen. Je hebt keuze uit: [add, get, export]: ")

if command_name != 'add' and command_name != 'get' and command_name != 'export':
	print("Foutief commando ingegeven")
	sys.exit(-1)




if command_name == 'add':
		abbrev_text = input("Wat is de afkorting die je wilt toevoegen? Bestaan uit 2 initialen in uppercase: ")
		#Ik had hier eventueel nog een check kunnen schrijven zodat er enkel letters zijn, 
		#maar ik ga er van uit dat dit out-of-scope if voor de opdracht.
		while len(abbrev_text) != 2:
			abbrev_text = input("Gelieve een correcte input mee te geven. De afkorting bestaat uit 2 characters: ")
		abbrev_id = input("Geef een ID mee: ")
		commands.add_abbrev(abbrev_id,abbrev_text)
		commands.close()
if command_name == 'get':
		abbrev_id = input("Geef een ID mee: ")
		commands.get_abbrev_by_id(abbrev_id)
		commands.close()
if command_name == 'export':

		csv_file = input("Geef de volledige benaming van het CSV bestand: ")
		# Geef gebruiker keuze om csv zelf toe te voegen of niet.
		if not csv_file.endswith(".csv"):
			csv_file += '.csv'

		table_name = input("Geef de tabelnaam die geëxporteerd moet worden: ")
		commands.export_table_to_csv_file(csv_file,table_name)