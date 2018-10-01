"""
Main file containing thhe application logic
"""
from datetime import datetime

comments = []
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

	def logout(self):
		"""this returns the user name and the time they logged out"""
		logout_details = ("{} logged out at {}".format(self.name, self.lastLoggedInAt))
		return login_details		

class Comment(object):
    """This class holds methods for adding, 
    modifying, deleting and replying to a comment
    """
    def __init__(self,name,comment):
        self.name = name
        self.comment = comment
        self.id = len(comments) + 1


    def add(self):
        """
        This funtion adds a comment and name to the list
        """
        holder = {}

        holder['id'] = self.id
        holder['name'] = self.name
        holder['comment'] = self.comment
        holder['Time'] = datetime.now()
        
        comments.append(holder)
        return comments

    def delete(self,name):
        """
        This function deletes comment from the list
        """    
        for id in self.comment:
            if id in id['id']:
                del(self.comment['comment'])
                return self.comment
