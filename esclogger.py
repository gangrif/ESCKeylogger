"""
Copyright (c) 2015, Aman Deep
All rights reserved.

ESC Key mods by Nate, @gangrif

A simple ESCAPE keylogger witten in python for linux platform

Notes from Gangrif, I've changed the 'grave key' to F11
"""

import pyxhook
c=0
print "This logger will only count the number of times you press ESC. \n\t\tPress F11 (Function key 11) to exit\n\n"

#this function is called everytime a key is pressed.
def OnKeyPress(event):
  #Because, WTF python?
  global c

  if event.Ascii==200: #200 is the ascii value of the grave key F11
    print "Your ESC Count was: %s" % c
    new_hook.cancel()

  if event.Ascii==27: #This is for esc
    c += 1


#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
