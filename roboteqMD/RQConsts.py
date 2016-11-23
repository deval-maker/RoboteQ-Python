#!/usr/bin/env python

# Command Prefixes
PREF_SETCMD = "!"
PREF_SETCONF = "^"
PREF_GETVAL = "?"
PREF_GETCONF = "!"
PREF_MAINT = "%"
PREF_HISTORY = "#"

# Default PassKey for few "risky" maintenance commands
DEF_KEY = "321654987"

# List of available Configuration Commands/Queries
_MMOD = "MMOD"
_MAC = "MAC"
_MDEC = "MDEC"

# List of available RunTime Commands/Queries
_GO = "GO"
_CB = "CB"
_DI = "DI"

# List of available Maintenance Commands
_RESET = "RESET"
_SLD = "SLD"
_EESAV = "EESAV"

if __name__ == '__main__':
	print ("Roboteq Constants defined !!")
