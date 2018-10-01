"""
Main file containing thhe application logic
"""
from datetime import datetime
class Users:
	def __init__(self, name, role):
		"""Initializes the Users class"""
		self.name  = name
		self.role = role
		self.lastLoggedInAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

	def login(self):
		"""this returns the user name and the time they logged in"""
		login_details = ("{} logged in at {}".format(self.name, self.lastLoggedInAt))
		return login_details 
