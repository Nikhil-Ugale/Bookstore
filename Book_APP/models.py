from Book_APP import db

class Book_Table(db.Model):
    ___tablename__ = 'Book'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    author = db.Column(db.Text)
    
    def __init__(self,name,author):
        self.name = name
        self.author = author
        
    def __repr__(self):
        return f"Name of Book:{self.name}; Author name:{self.author}"