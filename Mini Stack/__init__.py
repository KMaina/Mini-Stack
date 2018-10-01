from datetime import datetime

class Comment(object):
    """This class holds methods for adding, 
    modifying, deleting and replying to a comment
    """
    def __init__(self):
        self.comment = []

    def add(self,name,comment):
        """
        This funtion adds a comment and name to the list
        """
        holder = {}

        holder['name'] = name
        holder['comment'] = comment
        holder['id'] = len(self.comment)+1
        holder['Time'] = datetime.datetime.now()
        self.comment.append(holder)
        return self.comment

    def delete(self,name):
        """
        This function deletes comment from the list
        """    
        for id in self.comment:
            if id in id['id']:
                del(self.comment['comment'])
                return self.comment

if __name__ == '__main__':
    a = Comment().add("Clint","My name is Clint")
    d = Comment().add("Ken","This is my comment")
    b = Comment().delete("Clint")
    print (d)