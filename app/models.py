from app import db

# Our book table class
class Book(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    # Relationship with reviews
    reviews = db.relationship('Review', backref='books', lazy=True)

    # Converting the attributes of an instance of the class into a dictionary format
    def to_dict(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'summary': self.summary,
            'genre': self.genre
        }
    # A readable string representation of a book object, displaying its title.
    def __repr__(self):
        return f'<books {self.title}>'

# Our Review table class
class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'), nullable=False)
    user = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {           
            'book_id': self.book_id,
            'user': self.user,
            'rating': self.rating,
            'review_text': self.review_text
        }
    # Same as above but representating of reviews showing the user and associated Book ID
    def __repr__(self):
        return f'<Review by {self.user} for Book ID {self.book_id}>'
