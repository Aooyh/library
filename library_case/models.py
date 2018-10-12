from library_case.library_app import db

medium_table = db.Table('mid_tab',
                        db.Column('author_id', db.Integer, db.ForeignKey('authors.id')),
                        db.Column('book_id', db.Integer, db.ForeignKey('books.id')))

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '作者: %s' % self.name


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    authors = db.relationship('Author', secondary='mid_tab', backref='books')

    def __repr__(self):
        return '%s' % self.name

# class Book(db.Model):
#     __tablename__ = 'authors'
#     id = db.Column(db.Integer,primary_key=True)
