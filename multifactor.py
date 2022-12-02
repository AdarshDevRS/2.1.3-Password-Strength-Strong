# a213_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restricted app
my_auth = mfg.MultiFactorAuth()

# set the users authentication information
question = "How many chairs are in your house and what color is each of them?"
answer = "3, red, blue, green"
my_auth.set_authentication(question, answer)

# start the GUI
my_auth.mainloop()
