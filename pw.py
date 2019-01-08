#!/usr/bin/python
#playing with password locker program - this is insecure

import sys, pyperclip

PASSWORDS = {'email': 'asdfsdsg23423fsdvzsdg032u319', 'blog': 'w3etrrdfsdfs8ueue73ujsj', 'suitcase':'12345'}



if len(sys.argv) < 2: #just in case you forgot to add the name of the first account in the dictionary
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account]) #this will copy the value of the account key
	print('password has been copied to the clipboard')

else:
	print('there are no account named' + account)
