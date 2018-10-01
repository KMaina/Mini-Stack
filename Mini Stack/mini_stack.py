from datetime import datetime

comments = []
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

if __name__ == '__main__':
    a = Comment("Clint","My namenkpho").add()
    b = Comment("ken","My lkasdblkjb").add()
    print (b)