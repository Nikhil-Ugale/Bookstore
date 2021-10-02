from Book_APP import db

class Book_Table(db.Model):
    ___tablename__ = 'Book'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    author = db.Column(db.Text)
    price = db.Column(db.Integer)
    
    def __init__(self,name,author,price):
        self.name = name
        self.author = author
        self.price = price
        
   
    def __repr__(self):
        return ("Name of Book:{}\n"
                 "Author name:{}"
                 "Book Price".format(self.name,self.author,self.price))
       
         
            