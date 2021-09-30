from Book_APP.models import Book_Table
from Book_APP import db

def test_book():
    newbook = Book_Table('three point someone','chetan ')

    db.session.add(newbook)
    db.session.commit()
   

    books = Book_Table.query.all()
    for book in books:
        print(book)
        #assert(1==1)

    # db.session.delete(newbook)
    # db.session.commit()
    
    assert newbook.name == 'three point someone'


