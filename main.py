import sys


from app.commands import Commands


script_naam, command_name = sys.argv


commands = Commands('./data/car_crashes.db')

commands.get_abbrev_by_id('1')
