import sys


from app.commands import Commands


script_naam, command_name, abbrev_id, abbrev_text = sys.argv


commands = Commands('./data/car_crashes.db')


if command_name == 'add':
		commands.add_abbrev(abbrev_id,abbrev_text)